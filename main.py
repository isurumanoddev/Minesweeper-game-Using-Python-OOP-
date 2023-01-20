from tkinter import *
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
left_frame = Frame(window, width=utils.width_percentage(15), height=utils.height_percentage(85), bg="#07A831")
left_frame.place(x=0, y=utils.height_percentage(15))
center_frame = Frame(window, bg="#976F0D", width=utils.width_percentage(85), height=utils.height_percentage(85))
center_frame.place(x=utils.width_percentage(15), y=utils.height_percentage(15))


for row in range(7):
    for column in range(11):
        c = Cell(row, column)
        c.create_button_object(center_frame)
        c.cell_btn_object.grid(row=row, column=column)

Cell.randomize_mine()
# for cell in Cell.all:
#     print(cell, cell.is_mine)

window.mainloop()
