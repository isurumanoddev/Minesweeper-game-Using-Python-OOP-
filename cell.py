import random
from tkinter import *
import settings


class Cell:
    all = []
    create_cell_count_label_ = None
    cell_count = 70

    def __init__(self, x, y, is_mine=False):
        self.y = y
        self.x = x
        self.is_mine = is_mine
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_button(self, location):
        button = Button(location, text="", font=("", 20), width=3, height=1, bg="yellow")
        self.cell_btn_object = button
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_count == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()
        # Cell.create_cell_count_label_.config(text=f"Cells left{Cell.cell_count}")

    def right_click_action(self, event):
        print("Right Click")
        self.get_cell_by_axis(self.x, self.y)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, int(settings.MINES_COUNT))
        for cell in picked_cells:
            cell.is_mine = True

    @staticmethod
    def create_cell_count_label(location):
        label = Label(location, text=f"Cells Left 70", font=("", 15), width=20)
        Cell.create_cell_count_label_ = label

    def show_mine(self):
        self.cell_btn_object.config(bg="red")

    def show_cell(self):
        Cell.cell_count -= 1

        self.cell_btn_object.config(bg="green", text=f"{self.surrounded_cells_mine_count}")
        Cell.create_cell_count_label_.config(text=f"Cells left{Cell.cell_count}")

    @property
    def surrounded_cells_mine_count(self):
        mine_count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                mine_count += 1
        return mine_count

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                # cell.cell_btn_object.config(bg="green")
                return cell

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

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
