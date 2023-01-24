import random
from tkinter import *
import settings
import ctypes


class Cell:
    all = []
    ramaining_cell_label = None
    ramaining_mine_candidate_label = None
    remaining_cell_count = 99
    ramaining_mine_candidate_count = 15

    def __init__(self, x, y, is_mine=False):
        self.y = y
        self.x = x
        self.is_open = False
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.button_object = None
        Cell.all.append(self)

    def create_btn_object(self, location):
        button = Button(location, text="", font=("", 14), width=5, height=1, fg="white", bg="black")
        self.button_object = button
        button.bind("<Button-1>", self.click_left_actions)
        button.bind("<Button-3>", self.click_right_actions)

    def click_left_actions(self, event):
        if not self.is_mine_candidate:

            if self.is_mine:
                self.show_mine()
            else:
                self.show_cell()
                if self.surrounded_cells_mines_lenghth() == 0:
                    for cell in self.surrounded_cell:
                        cell.show_cell()

    @staticmethod
    def cell_count_label(location):
        label = Label(location, text="Reamining cells : 99", font=("", 12), width=40, height=2, fg="white", bg="green")
        Cell.ramaining_cell_label = label

    @staticmethod
    def mine_candidate_count_label(location):
        label = Label(location, text="Reamining mines : 15", font=("", 12), width=40, height=2, fg="white", bg="green")
        Cell.ramaining_mine_candidate_label = label

    # def check_mines(self):
    #     for cell in self.surrounded_cell:
    #         if cell.is_mine == True:
    #             print("mines")

    def show_mine(self):
        self.button_object.config(bg="red", fg="black")

    def show_cell(self):

        if self.is_open == False:
            Cell.remaining_cell_count -= 1
            print(Cell.ramaining_cell_label)
            self.button_object.config(bg="yellow", fg="black", text=f"{self.surrounded_cells_mines_lenghth()}")
            Cell.ramaining_cell_label.config(text=f"Reamining cells {Cell.remaining_cell_count}")
            self.is_open = True

    def surrounded_cells_mines_lenghth(self):
        mine_count = 0
        for mine in self.surrounded_cell:
            if mine.is_mine:
                mine_count += 1
        return mine_count

    def click_right_actions(self, event):
        if not self.is_mine_candidate:
            if not self.is_open:

                Cell.ramaining_mine_candidate_count -= 1
                self.button_object.config(bg="orange")
                Cell.ramaining_mine_candidate_label.config(text=f"Reamining cells {Cell.ramaining_mine_candidate_count}"
                                                           )
                self.is_mine_candidate = True

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cell(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @staticmethod
    def random_mines():
        random_sample = random.sample(Cell.all, int(settings.MINES_COUNT))

        for mine in random_sample:
            mine.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
