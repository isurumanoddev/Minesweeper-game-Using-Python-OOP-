from tkinter import *
import settings
import utils

window = Tk()
window.configure(bg="black")
window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
window.title("Minesweeper Games")
window.resizable(False, False)
frame = Frame(window, bg="red", width=settings.WIDTH, height=utils.height_percentage(25))
frame.place(x=0, y=0)
left_frame = Frame(window, width=150, height=utils.height_percentage(75), bg="green")
left_frame.place(x=0, y=180)

window.mainloop()

