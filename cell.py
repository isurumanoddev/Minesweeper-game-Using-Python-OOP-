import random
from tkinter import *
import settings


class Cell:
    all = []
    cell_count_object = None

    def __init__(self, is_mine=False):
        self.is_mine = is_mine
