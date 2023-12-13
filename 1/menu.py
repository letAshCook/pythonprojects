import tkinter as tk  # change tkinter to tk
from TicTacToe import *


class menu(object):

    win = tk.Tk()  # create window
    win.title("gui")  # title name

    win.geometry("800x800")  # window size
    win.resizable(0, 0)  # lock winow size
    win.config(background="skyblue")  # change background color

    # icon
    # win.iconbitmap("")

    # button image
    # img = Photoimage(file="")
    # btn.config(image= img)
    def loginCheck(self):
        self.page.destroy()
        TicTacToe(self.root)

    btn = tk.Button(text="stear", command=loginCheck.self)  # create button
    btn.config(bg="red")  # button color
    btn.config(width=10, height=5)  # button size
    btn.pack()

    win.mainloop()  # window display
