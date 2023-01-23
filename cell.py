import random
from tkinter import *
import settings
import ctypes


class Cell:
    all = []
    create_cell_count_label_ = None
    mine_count_label_ = None
    cell_count = 70
    mine_candidate_count = 10

    def __init__(self, x, y, is_mine=False):
        self.y = y
        self.x = x
        self.is_open = False
        self.is_mine_candidate = False
        self.is_mine = is_mine
        self.cell_btn_object = None

        Cell.all.append(self)

    def test_button(self, location):
        test_button = Button(location, text="asdsadsad", bg="red")
        self.btn_object = test_button

    def create_button(self, location):
        button = Button(location, text="", font=("", 20), width=3, height=1, bg="black")
        self.cell_btn_object = button
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)

    def left_click_action(self, event):
        if not self.is_mine_candidate:
            if self.is_mine:
                self.show_mine()
                self.disable_buttons()

            else:
                if self.surrounded_cells_mine_count == 0:
                    for cell in self.surrounded_cells:
                        cell.show_cell()
                self.show_cell()
                if Cell.cell_count == settings.MINES_COUNT:
                    ctypes.windll.user32.MessageBoxW(0, "Congratulations", "Game over", 0)


    def disable_buttons(self):
        for cell in Cell.all:
            cell.cell_btn_object.config(state=DISABLED)

    def right_click_action(self, event):
        if not self.is_open:
            print("Right Click")
            if not self.is_mine_candidate:
                self.cell_btn_object.config(bg="orange")
                self.is_mine_candidate = True
                Cell.mine_candidate_count -= 1
                Cell.mine_count_label_.config(text=f"Cells left{Cell.mine_candidate_count}")
            else:
                self.cell_btn_object.config(bg="black")
                self.is_mine_candidate = False
                Cell.mine_candidate_count += 1
                Cell.mine_count_label_.config(text=f"Cells left{Cell.mine_candidate_count}")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, int(settings.MINES_COUNT))
        for cell in picked_cells:
            cell.is_mine = True

    @staticmethod
    def create_cell_count_label(location):
        label = Label(location, text=f"Cells Left 70", font=("", 15), width=20)
        Cell.create_cell_count_label_ = label

    @staticmethod
    def create_mine_count_label(location):
        label = Label(location, text=f"Cells Left 10", font=("", 15), width=20)
        Cell.mine_count_label_ = label

    def show_mine(self):
        self.cell_btn_object.config(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "you clicked on a mine", "Game over", 0)

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1

        self.cell_btn_object.config(bg="green", text=f"{self.surrounded_cells_mine_count}", foreground="black")
        Cell.create_cell_count_label_.config(text=f"Cells left{Cell.cell_count}")
        self.is_open = True

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
