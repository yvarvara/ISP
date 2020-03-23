from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from new_picture_page import NewPicturePage
from drawing_page import GameType


class MainView:
    def __init__(self, root):

        self.var_type_game = IntVar()
        self.root = root
        button1 = Button(root, text="Settings", bg='#fafafa', command=self.settings_click)
        button1.grid(column=1, row=0, pady=20, padx=20)
        button2 = Button(root, text="New picture", bg='#fafafa', command=self.new_picture_click)
        button2.grid(column=1, row=0, pady=20, padx=20, sticky=E)

        self.pictures_number = 16
        self.type_game = GameType.CLASSIC.value

        self.show_pictures()

    def settings_click(self):
        top = Toplevel()
        top['bg'] = '#00363a'
        top.geometry('400x400')

        style = ttk.Style()
        style.configure('Style.TRadiobutton', background='#fafafa')

        label = Label(top, text='  Game type:', bg='#fafafa', anchor='w')
        label.place(relx=0.25, rely=0.2, relwidth=0.5)

        r_button1 = ttk.Radiobutton(top, text='Easy', variable=self.var_type_game,
                                    value=GameType.EASY.value, command=self.selected,
                                    style='Style.TRadiobutton')
        r_button2 = ttk.Radiobutton(top, text='Classic', variable=self.var_type_game,
                                    value=GameType.CLASSIC.value, command=self.selected,
                                    style='Style.TRadiobutton')
        r_button3 = ttk.Radiobutton(top, text='Hard', variable=self.var_type_game,
                                    value=GameType.HARD.value, command=self.selected,
                                    style='Style.TRadiobutton')

        r_button1.place(relx=0.25, rely=0.25, relheight=0.2, relwidth=0.5)
        r_button2.place(relx=0.25, rely=0.45, relheight=0.2, relwidth=0.5)
        r_button3.place(relx=0.25, rely=0.65, relheight=0.2, relwidth=0.5)

        self.var_type_game.set(self.type_game)

    def selected(self, *args):
        self.type_game = self.var_type_game.get()

    def new_picture_click(self):
        file_path = askopenfilename()
        NewPicturePage(Toplevel(), file_path, self.var_type_game.get())

    def show_pictures(self):
        frame = Frame(self.root)
        frame.grid(column=0, row=1, columnspan=2)

        c = Canvas(frame, width=683, height=800, scrollregion=(0, 0, 0, 255 * ((self.pictures_number + 1) // 2)),
                   bg='#006064')
        c.grid(column=0, row=0)

        v_bar = ttk.Scrollbar(frame, orient=VERTICAL)
        v_bar.grid(column=1, row=0, rowspan=(self.pictures_number + 1) // 2, sticky='ns')

        c.config(yscrollcommand=v_bar.set)
        v_bar['command'] = c.yview

        interior = Frame(c, bg='#006064')
        c.create_window(0, 0, window=interior, anchor=NW)

        for i in range((self.pictures_number + 1) // 2):
            for j in range(2):
                if i * 2 + j == self.pictures_number:
                    break

                image_frame = Frame(interior)
                canvas = Canvas(image_frame, width=300, height=200, bg='white')
                canvas.pack()
                image_frame.grid(row=i, column=j, padx=20, pady=20)


if __name__ == "__main__":
    root = Tk()
    MainView(root)
    root.geometry("700x800")
    root.resizable(False, False)
    root['bg'] = '#00363a'
    root.mainloop()

