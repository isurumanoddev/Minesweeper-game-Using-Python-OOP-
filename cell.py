import random
from tkinter import Button


class Cell:
    all = []

    def __init__(self, row, col, is_mine=False):
        self.col = col
        self.row = row
        self.is_mine = is_mine
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_button_object(self, location):
        button = Button(location, text=f"{self.row}, {self.col}", bg="yellow", height=2, width=8, font=("Arial", 20))
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
        picked_cells = random.sample(Cell.all, 9)
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f"Cell({self.row},{self.col})"
