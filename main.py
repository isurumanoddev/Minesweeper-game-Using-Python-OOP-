from tkinter import *

import cell
from cell import Cell
import settings
import utils

window = Tk()
window.configure(bg="black")
window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
window.title("Minesweeper Games")
window.resizable(False, False)
frame = Frame(window, bg="#4F1D92", width=settings.WIDTH, height=utils.height_percentage(15))
frame.place(x=0, y=0)
center_frame = Frame(window, bg="#976F0D", width=utils.width_percentage(100), height=utils.height_percentage(85))
center_frame.place(x=utils.width_percentage(0), y=utils.height_percentage(15))



label = Label(frame, bg="black", fg="white", text="Minesweeper Game", font=("", 20))
label.place(x=200,y=0)
window.mainloop()
