from tkinter import *
from random import *

# Constants
WIDTH = 500
HEIGHT = 500

SIZE = 50

class Board(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, width = WIDTH, height = HEIGHT, background = "SpringGreen3")
        self.parent = parent
        self.initGame()
        self.pack()

    def initGame(self):
        self.createCat()

    def createCat(self):
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        self.create_oval(x, y, x + SIZE, y + SIZE, fill = "peach puff")


class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title = "Cotique"
        self.board = Board(parent)
        self.pack()


def main():
    root = Tk()
    game = Game(root)
    root.mainloop()

if __name__ == '__main__':
    main()