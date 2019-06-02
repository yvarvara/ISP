from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk
from pixelation import *
from drawing_page import DrawingPage, TypeGame


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)


class MainView(Page):
    def slider_move(self, *args):
        self.number_color = self.scale.get()

        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.top.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.top, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.top.image, anchor=NW)
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

        self.top.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.top, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.top.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)

    def on_click_button(self):
        DrawingPage(Toplevel(), self.pixelation, TypeGame.HARD)
        self.top.destroy()

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        self.number_color = 10
        self.size_block = 10

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack()
        container.pack(side="top", fill="both", expand=True)

        b2 = Button(buttonframe, text="New picture", command=self.new_window)
        b2.pack()

        p1.show()

    def selected(self, *args):
        self.pixelation = Pixelation(self.file_path, self.size_block, self.number_color, self.var_type_pixelation.get())
        self.pixelation.process_image()

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.top.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.top, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.top.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)

    def new_window(self):
        self.file_path = askopenfilename()

        top = Toplevel()
        top.geometry('900x600')

        self.top = top

        self.number_color = 10
        self.scale = Scale(top, orient=HORIZONTAL, label='Number of colors:', length=300, from_=10, to=100,
                           resolution=10, command=self.slider_move)
        self.scale.place(relx=0.05, rely=0.1)

        self.size_block = 10
        self.scale1 = Scale(top, orient=HORIZONTAL, length=300, from_=10, to=50, resolution=5,
                            command=self.change_size_block, label='New Pixel Size:')
        self.scale1.place(relx=0.05, rely=0.25)

        label = Label(top, text='Сlustering method:')
        label.place(relx=0.05, rely=0.4)

        self.var_type_pixelation = IntVar()

        r_button1 = ttk.Radiobutton(top, text='K-means', variable=self.var_type_pixelation,
                                    value=TypePixelation.K_AVERAGE_RANDOM_POINT.value, command=self.selected)
        r_button2 = ttk.Radiobutton(top, text='Modified K-means', variable=self.var_type_pixelation,
                                    value=TypePixelation.K_AVERAGE_POPULAR_POINT.value, command=self.selected)
        r_button3 = ttk.Radiobutton(top, text='K-means (scikit learn)', variable=self.var_type_pixelation,
                                    value=TypePixelation.NEURAL_NETWORK.value, command=self.selected)
        r_button4 = ttk.Radiobutton(top, text='Original', variable=self.var_type_pixelation,
                                    value=TypePixelation.NONE.value, command=self.selected)

        self.var_type_pixelation.set(TypePixelation.NONE.value)
        self.pixelation = Pixelation(self.file_path, 10, 10, self.var_type_pixelation.get())
        self.pixelation.process_image()

        r_button1.place(relx=0.05, rely=0.45, relheight=0.1, relwidth=0.4)
        r_button2.place(relx=0.05, rely=0.55, relheight=0.1, relwidth=0.4)
        r_button3.place(relx=0.05, rely=0.65, relheight=0.1, relwidth=0.4)
        r_button4.place(relx=0.05, rely=0.75, relheight=0.1, relwidth=0.4)

        button = Button(top, text='Draw!', command=self.on_click_button)
        button.place(relx=0.2, rely=0.85)

        base_width = 450
        img = self.pixelation.image
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size))

        self.top.image = ImageTk.PhotoImage(img)

        canvas = Canvas(self.top, width=450, height=h_size)
        canvas.create_image(0, 0, image=self.top.image, anchor=NW)
        canvas.place(relx=0.45, rely=0.1)


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")

    root.mainloop()



