from enum import Enum
from tkinter import *
from tkinter import ttk

from colors import ColorsMethods


class TypeGame(Enum):
    CLASSIC = 0
    EASY = 1  
    HARD = 2    


class DrawingPage():
    SCALE = 1
    SCALE_MAX = 5
    SCALE_MIN = 1
    ERROR_MAX = 10

    def __init__(self, root, pixelation, type_game):

        self.root = root

        self.type_game = type_game
        self.size_block = pixelation.size_block
        self.color_number = len(pixelation.get_colors())
        self.colors = pixelation.get_colors()
        self.pixels = pixelation.pixels
        self.pixelation = pixelation
        self.error_clicks = 0

        self.is_draw = []
        for i in range(pixelation.number_blocks_in_width):
            self.is_draw.append([0 for j in range(pixelation.number_blocks_in_height)])

        for i in range(len(self.colors)):
            self.colors[i] = ColorsMethods.rgb_to_hex(*self.colors[i])
        
        self.current_color = self.colors[0]

        self.width = pixelation.width // self.size_block * self.size_block
        self.height = pixelation.height // self.size_block * self.size_block

        self.h_bar = ttk.Scrollbar(root, orient=HORIZONTAL)
        self.h_bar.grid(column=0, row=1, sticky='we')
        self.v_bar = ttk.Scrollbar(root, orient=VERTICAL)
        self.v_bar.grid(column=1, row=0, sticky='ns')

        self.canvas = Canvas(root, width=self.width, height=self.height, bg='white',
                             scrollregion=(0, 0, self.width, self.height))

        self.canvas.bind("<Button-4>", self.zoom_increase)
        self.canvas.bind("<Button-5>", self.zoom_decrease)

        self.canvas.grid(column=0, row=0, sticky='nsew')
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.canvas.config(xscrollcommand=self.h_bar.set, yscrollcommand=self.v_bar.set)
        self.h_bar['command'] = self.canvas.xview
        self.v_bar['command'] = self.canvas.yview

        self.create_field()
        self.create_palette()

    def create_field(self):
        for i in range(self.width // self.size_block):
            self.canvas.create_line(self.size_block * i, 0, self.size_block * i, self.height)

            for j in range(self.height // self.size_block):
                color = ColorsMethods.rgb_to_hex(*self.pixels[self.size_block // 2 + self.size_block * i,
                                        self.size_block // 2 + self.size_block * j])

                self.text_size = self.size_block // 3

                text = str(self.colors.index(color) + 1)
                self.canvas.create_text(self.size_block // 2 + self.size_block * i,
                                        self.size_block // 2 + self.size_block * j,
                                        text=text, font=("Purisa", self.text_size),
                                        tags='color_num')

            self.canvas.create_line(self.size_block * (i + 1), 0, self.size_block * (i + 1), self.height)

        for i in range(0, self.height // self.size_block + 1):
            self.canvas.create_line(0, self.size_block * i, self.width, self.size_block * i)

        self.canvas.bind('<B1-Motion>', self.block_fill)
        self.canvas.bind('<Button-1>', self.block_fill)

    def create_palette(self):
        frame = Frame(self.root, width=self.width)
        frame.grid(column=0, row=2, sticky='we')

        c = Canvas(frame, width=self.width, height=60, bg='#f2f2f2',
                   scrollregion=(0, 0, self.color_number * 67, self.height))

        c.grid(column=0, columnspan=5, row=0, sticky='we')

        h_bar = ttk.Scrollbar(frame, orient=HORIZONTAL)
        h_bar.grid(column=0, columnspan=5, row=1, sticky='we')

        c.config(xscrollcommand=h_bar.set)
        h_bar['command'] = c.xview

        interior = Frame(c, bg='#f2f2f2')
        c.create_window(0, 0, window=interior, anchor=NW)

        for i in range(1, self.color_number + 1):
            color = self.colors[i - 1]
            inversed_color = ColorsMethods.color_inverse(color)

            btn = Button(interior, width=2, text=str(i), font=('Purisa', '12', 'bold'), height=1,
                         background=color, foreground=inversed_color, bd=3)
            if i == 1:
                btn['relief'] = SUNKEN
                self.prev_button = btn

            btn.config(command=lambda button=btn: self.set_current_color(button))
            btn.grid(column=i - 1, row=0, padx=5, pady=5)

    def block_fill(self, event):
        size_block = self.size_block * self.SCALE
        x_click = (self.canvas.canvasx(event.x))
        y_click = (self.canvas.canvasy(event.y))

        if not (0 < x_click / self.SCALE < self.width and 0 < y_click / self.SCALE < self.height):
            return

        if ColorsMethods.rgb_to_hex(*self.pixels[x_click / self.SCALE, y_click / self.SCALE]) != self.current_color:
            if self.type_game == TypeGame.HARD:
                self.error_clicks += 1
                if self.error_clicks == self.ERROR_MAX:
                    DrawingPage(Toplevel(), self.pixelation, TypeGame.HARD)
                    self.root.destroy()
            return

        self.is_draw[int(int(x_click / self.SCALE + 0.00001) // size_block)][int(int(y_click / self.SCALE + 0.00001) // size_block)] = 1

        x = x_click // size_block * size_block
        y = y_click // size_block * size_block

        self.canvas.create_rectangle(x, y, x + size_block, y + size_block,
                                     fill=self.current_color, outline=self.current_color)

    def set_current_color(self, button):
        self.current_color = button['bg']

        self.prev_button['relief'] = RAISED

        button['relief'] = SUNKEN
        self.prev_button = button

    def zoom_increase(self, *args):
        if self.SCALE * 1.1 > self.SCALE_MAX:
            return

        self.canvas.scale("all", 0, 0, 1.1, 1.1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.text_size *= 1.1
        self.canvas.itemconfigure('color_num', font=('Purisa', int(self.text_size)))
        self.SCALE *= 1.1

    def zoom_decrease(self, *args):
        if self.SCALE * 0.9 < self.SCALE_MIN:
            return

        self.canvas.scale("all", 0, 0, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.text_size *= 0.9
        self.canvas.itemconfigure('color_num', font=('Purisa', int(self.text_size)))
        self.SCALE *= 0.9
