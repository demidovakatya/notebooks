# Works in Python 3.x.
# Creates a calculator grid.
# It isn't supposed to work as a calculator.

from tkinter import *
from tkinter.ttk import *

class Calc(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator Grid")
        Style().configure('TButton', padding = (0, 5, 0, 5), font = "serif 10")

        # Create the grid
        self.columnconfigure(0, pad = 3)
        self.columnconfigure(1, pad = 3)
        self.columnconfigure(2, pad = 3)
        self.columnconfigure(3, pad = 3)

        self.rowconfigure(0, pad = 3)
        self.rowconfigure(1, pad = 3)
        self.rowconfigure(2, pad = 3)
        self.rowconfigure(3, pad = 3)
        self.rowconfigure(4, pad = 3)
        self.rowconfigure(5, pad = 3)

        entry = Entry(self)
        entry.grid(row = 0, columnspan = 4, sticky = W+E)

        clr = Button(self, text = "C")
        clr.grid(row = 1, column = 0)
        back = Button(self, text = "BACK")
        back.grid(row = 1, column = 1)
        close = Button(self, text = "EXIT", command = self.quit)
        close.grid(row = 1, column = 2)
        div = Button(self, text = "/")
        div.grid(row = 1, column = 3)

        seven = Button(self, text = "7")
        seven.grid(row = 2, column = 0)
        eight = Button(self, text = "8")
        eight.grid(row = 2, column = 1)
        nine = Button(self, text = "9")
        nine.grid(row = 2, column = 2)
        mult = Button(self, text = "*")
        mult.grid(row = 2, column = 3)

        four = Button(self, text = "4")
        four.grid(row = 3, column = 0)
        five = Button(self, text = "5")
        five.grid(row = 3, column = 1)
        six = Button(self, text = "6")
        six.grid(row = 3, column = 2)
        mns = Button(self, text = "-")
        mns.grid(row = 3, column = 3)

        one = Button(self, text = "1")
        one.grid(row = 4, column = 0)
        two = Button(self, text = "2")
        two.grid(row = 4, column = 1)
        three = Button(self, text = "3")
        three.grid(row = 4, column = 2)
        pls = Button(self, text = "+")
        pls.grid(row = 4, column = 3)


        zero = Button(self, text = "0")
        zero.grid(row = 5, column = 0)
        dot = Button(self, text = ".")
        dot.grid(row = 5, column = 1)
        equal = Button(self, text = "=")
        equal.grid(row = 5, column = 2, columnspan = 2)

        self.pack()

def main():
    root = Tk()
    app = Calc(root)
    root.mainloop()

if __name__ == '__main__':
    main()