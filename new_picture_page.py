from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from pixelation import *
from drawing_page import DrawingPage, TypeGame


class NewPicturePage():
    def __init__(self, root, file_path):
        self.file_path = file_path
        self.root = root

        self.root.geometry('900x600')

        self.number_color = 10
        self.scale = Scale(root, orient=HORIZONTAL, label='Number of colors:', length=300, from_=10, to=100,
                           resolution=10, command=self.slider_move)
        self.scale.place(relx=0.05, rely=0.1)

        self.size_block = 10
        self.scale1 = Scale(root, orient=HORIZONTAL, length=300, from_=10, to=50, resolution=5,
                            command=self.change_size_block, label='New Pixel Size:')
        self.scale1.place(relx=0.05, rely=0.25)

        label = Label(root, text='Сlustering method:')
        label.place(relx=0.05, rely=0.4)

        self.var_type_pixelation = IntVar()

        r_button1 = ttk.Radiobutton(root, text='K-means', variable=self.var_type_pixelation,
                                    value=TypePixelation.K_AVERAGE_RANDOM_POINT.value, command=self.selected)
        r_button2 = ttk.Radiobutton(root, text='Modified K-means', variable=self.var_type_pixelation,
                                    value=TypePixelation.K_AVERAGE_POPULAR_POINT.value, command=self.selected)
        r_button3 = ttk.Radiobutton(root, text='K-means (scikit learn)', variable=self.var_type_pixelation,
                                    value=TypePixelation.NEURAL_NETWORK.value, command=self.selected)
        r_button4 = ttk.Radiobutton(root, text='Original', variable=self.var_type_pixelation,
                                    value=TypePixelation.NONE.value, command=self.selected)

        r_button1.place(relx=0.05, rely=0.45, relheight=0.1, relwidth=0.4)
        r_button2.place(relx=0.05, rely=0.55, relheight=0.1, relwidth=0.4)
        r_button3.place(relx=0.05, rely=0.65, relheight=0.1, relwidth=0.4)
        r_button4.place(relx=0.05, rely=0.75, relheight=0.1, relwidth=0.4)

        self.var_type_pixelation.set(TypePixelation.NONE.value)
        self.pixelation = Pixelation(self.file_path, 10, 10, self.var_type_pixelation.get())
        self.pixelation.process_image()

        button = Button(root, text='Draw!', command=self.on_click_button)
        button.place(relx=0.2, rely=0.85)

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

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.root.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.root.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)

    def change_size_block(self, *args):
        self.size_block = self.scale1.get()

        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.root.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.root.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)

    def on_click_button(self):
        DrawingPage(Toplevel(), self.pixelation, TypeGame.CLASSIC)
        self.root.destroy()

    def selected(self, *args):
        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.root.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.root.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)