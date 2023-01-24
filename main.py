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
frame = Frame(window, bg="black", width=settings.WIDTH, height=utils.height_percentage(25))
frame.place(x=0, y=0)
center_frame = Frame(window, bg="#976F0D", width=utils.width_percentage(100), height=utils.height_percentage(75))
center_frame.place(x=utils.width_percentage(0), y=utils.height_percentage(25))

for row in range(9):
    for column in range(11):
        c = Cell(row,column)
        c.create_btn_object(center_frame)
        c.button_object.grid(row=row,column =column)
Cell.random_mines()
label = Label(frame, bg="black", fg="white", text="Minesweeper Game", font=("", 30))
label.place(x=150,y=0)
Cell.cell_count_label(frame)
Cell.ramaining_cell_label.place(x=0,y=77)
Cell.mine_candidate_count_label(frame)
Cell.ramaining_mine_candidate_label.place(x=355,y=77)

window.mainloop()
