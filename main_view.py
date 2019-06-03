from tkinter import *
from tkinter.filedialog import askopenfilename
from new_picture_page import NewPicturePage


class MainView():
    def __init__(self, root):

        self.root = root

        button = Button(root, text="New picture", command=self.new_picture_click)
        button.grid(column=0, row=0)

    def new_picture_click(self):
        file_path = askopenfilename()
        NewPicturePage(Toplevel(), file_path)


if __name__ == "__main__":
    root = Tk()
    MainView(root)
    root.wm_geometry("400x400")

    root.mainloop()

