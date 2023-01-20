from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_button_object(self, location):
        button = Button(location, text="button", bg="red", height=5, width=8)
        self.cell_btn_object = button

