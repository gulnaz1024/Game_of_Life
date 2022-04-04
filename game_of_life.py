from copy import deepcopy
import time
import os
import threading
import numpy as np
from random import randint
from tkinter.ttk import *
from tkinter import *


class Board():
    def __init__(self, width, height, on_values):
        on_values_max = np.array(on_values).max(axis=0)
        self.width = width+1
        self.height = height+1
        self.board_NP = np.zeros((self.height+1, self.width+1), dtype=int)
        self.on_values = on_values

        try:
            assert((on_values_max[0]) <= self.height)
        except AssertionError:
            print("one of the indices of your on_values exceeds board height")
            exit()
        try:
            assert(on_values_max[1] <= self.width)
        except AssertionError:
            print("one of the X indices of your on_values exceeds board width")
            exit()

        for i in on_values:
            self.board_NP[i[1]+1, i[0]+1] = 1

        print(self.board_NP)
        print("\n")

    def __str__(self):
        return str(self.board_NP)

    def live_on(self, cell):
        on = len(np.array(self.sub[cell[0]][cell[1]].nonzero()).transpose())
        if self.board_NP[cell[0]+1, cell[1]+1] == 1:
            on -= 1
        # # Any live cell with two or three live neighbours survives
        # if self.board_NP[cell[0]+1, cell[1]+1] == 1 and (on == 2 or on == 3):
        #     return True
        # # Any dead cell with three live neighbours becomes a live cell
        # elif self.board_NP[cell[0]+1, cell[1]+1] == 0 and on == 3:
        #     return True
        # else:
        #     return False

        # Any dead cell with 2 or 4 live neighbours becomes alive
        if self.board_NP[cell[0]+1, cell[1]+1] == 0 and (on == 2 or on == 4):
            return True
        # Any live cell with 3 live neighbours becomes a dead cell
        elif self.board_NP[cell[0]+1, cell[1]+1] == 1 and on == 3:
            return False
        else:
            return False

    def update(self):
        view = tuple(np.subtract(self.board_NP.shape, (3, 3)) + 1) + (3, 3)
        stride = self.board_NP.strides + self.board_NP.strides
        self.sub = np.lib.stride_tricks.as_strided(self.board_NP, view, stride)

        board_state = deepcopy(self.board_NP)

        for j in range(self.width-1):
            for i in range(self.height-1):
                if self.live_on([i, j]):
                    board_state[i+1, j+1] = 1
                else:
                    board_state[i+1, j+1] = 0

        self.board_NP = deepcopy(board_state)
        if not self.board_NP.any():
            for i in self.on_values:
                self.board_NP[i[1]+1, i[0]+1] = 1

    def draw(self):
        while True:
            os.system("cls")
            self.update()
            for row in self.board_NP:
                print(row)
            print("\n")
            try:
                for i in buttons:
                    for j in i:
                        j.configure(bg="grey")
                for i in np.array(self.board_NP.nonzero()).transpose():
                    buttons[i[0], i[1]].configure(bg="cyan")
            except IndexError:
                pass
            time.sleep(0.5)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x500")
    # colours = ['white', 'black']

    # cells = [[3, 1], [4, 3], [4, 2], [5, 4], [5, 3], [6, 4]]

    cells = []
    for i in range(randint(5, 15)):
        x = randint(1, 5)
        y = randint(1, 5)
        cells.append([x, y])
    demo_board = Board(9, 5, cells)

    buttons = []
    for i in range(demo_board.height+1):
        b = []
        for j in range(demo_board.width+1):
            button = Button(text='', width=6, height=4)
            button.grid(row=i, column=j)
            b.append(button)
        buttons.append(b)
        b = []
    buttons = np.array(buttons)

    # demo_board.draw()
    draw = threading.Thread(target=demo_board.draw)
    draw.daemon = True
    draw.start()
    root.mainloop()
