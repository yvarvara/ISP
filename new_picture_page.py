from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from pixelation import *
from drawing_page import DrawingPage, GameType


class NewPicturePage():
    def __init__(self, root, file_path, type_game):
        self.file_path = file_path
        self.root = root
        self.root['bg'] = '#006064'

        self.type_game = GameType(type_game)

        style = ttk.Style()
        style.configure('Style.TRadiobutton', background='#fafafa')

        self.root.geometry('900x600')

        self.number_color = 10
        self.scale = Scale(root, orient=HORIZONTAL, label='Number of colors:', length=270, from_=10, to=100,
                           resolution=10, command=self.slider_move, bg='#fafafa')
        self.scale.place(relx=0.05, rely=0.1)

        self.size_block = 10
        self.scale1 = Scale(root, orient=HORIZONTAL, length=270, from_=10, to=50, resolution=5,
                            command=self.change_size_block, label='New Pixel Size:', bg='#fafafa')
        self.scale1.place(relx=0.05, rely=0.25)

        label = Label(root, text='  Сlustering method:', bg='#fafafa', anchor='w')
        label.place(relx=0.05, rely=0.41, relwidth=0.3)

        self.var_type_pixelation = IntVar()

        r_button1 = ttk.Radiobutton(root, text='K-means', variable=self.var_type_pixelation,
                                    value=PixelationType.K_AVERAGE_RANDOM_POINT.value, command=self.selected,
                                    style='Style.TRadiobutton')
        r_button2 = ttk.Radiobutton(root, text='Modified K-means', variable=self.var_type_pixelation,
                                    value=PixelationType.K_AVERAGE_POPULAR_POINT.value, command=self.selected,
                                    style='Style.TRadiobutton')
        r_button3 = ttk.Radiobutton(root, text='K-means (ML)', variable=self.var_type_pixelation,
                                    value=PixelationType.NEURAL_NETWORK.value, command=self.selected,
                                    style='Style.TRadiobutton')
        r_button4 = ttk.Radiobutton(root, text='Original', variable=self.var_type_pixelation,
                                    value=PixelationType.NONE.value, command=self.selected,
                                    style='Style.TRadiobutton')

        r_button1.place(relx=0.05, rely=0.45, relheight=0.1, relwidth=0.3)
        r_button2.place(relx=0.05, rely=0.55, relheight=0.1, relwidth=0.3)
        r_button3.place(relx=0.05, rely=0.65, relheight=0.1, relwidth=0.3)
        r_button4.place(relx=0.05, rely=0.75, relheight=0.1, relwidth=0.3)

        self.var_type_pixelation.set(PixelationType.NONE.value)
        self.pixelation = Pixelation(self.file_path, 10, 10, self.var_type_pixelation.get())
        self.pixelation.process_image()

        button = Button(root, text='Draw!', command=self.on_click_button, bg='#fafafa')
        button.place(relx=0.05, rely=0.88)

        self.update_image()

    def update_image(self):
        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.root.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.root.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.2)

    def slider_move(self, *args):
        self.number_color = self.scale.get()

        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        self.update_image()

    def change_size_block(self, *args):
        self.size_block = self.scale1.get()

        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        self.update_image()

    def on_click_button(self):
        DrawingPage(Toplevel(), self.pixelation, self.type_game)
        self.root.destroy()

    def selected(self, *args):
        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        self.update_image()
