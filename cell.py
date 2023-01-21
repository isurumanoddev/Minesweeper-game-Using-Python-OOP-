import random
from tkinter import Button
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.y = y
        self.x = x
        self.is_mine = is_mine
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_button_object(self, location):
        button = Button(location, text=f" {self.x},{self.y}", bg="black", height=1, width=3, font=("Arial", 14),
                        foreground="white", borderwidth=6)
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)
        self.cell_btn_object = button

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()

        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        self.surrounded_cells_mines_count()
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    # @property
    def surrounded_cells_mines_count(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1
                cell.cell_btn_object.config(bg="#07A481")

            else:
                cell.cell_btn_object.config(bg="white", foreground="green", text=" ", )

        self.cell_btn_object.config(bg="#01E800", text=f"{count} ")

    def show_mine(self):
        self.cell_btn_object.config(bg="red")

    def right_click_action(self, event):
        print(event)
        print("Right click")

    @staticmethod
    def randomize_mine():
        picked_cells = random.sample(Cell.all, int(settings.MINES_COUNT))
        for i in picked_cells:
            i.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
