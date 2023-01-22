import random
from tkinter import *
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.y = y
        self.x = x
        self.is_mine = is_mine
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_button(self, location):
        button = Button(location, text=f"{self.x},{self.y}", font=("", 20), width=3, height=1, bg="yellow")
        self.cell_btn_object = button
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)

    def left_click_action(self, event):
        print("left Click")

    def right_click_action(self, event):
        print("Right Click")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
