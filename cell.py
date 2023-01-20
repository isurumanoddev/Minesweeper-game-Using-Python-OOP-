import random
from tkinter import Button

import settings


class Cell:
    all = []

    def __init__(self, row, col, is_mine=False):
        self.col = col
        self.row = row
        self.is_mine = is_mine
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_button_object(self, location):
        button = Button(location, text=f"{self.row}, {self.col}", bg="black", height=1, width=4, font=("Arial", 30),foreground="white",borderwidth=6)
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)
        self.cell_btn_object = button

    def left_click_action(self, event):
        print(event)
        print("left click")

    def right_click_action(self, event):
        print(event)
        print("Right click")

    @staticmethod
    def randomize_mine():
        picked_cells = random.sample(Cell.all, int(settings.MINES_COUNT))
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f"Cell({self.row},{self.col})"
