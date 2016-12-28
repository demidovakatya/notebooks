# Simple program that generates circles
# Works in Python 3.5

from random import *
from tkinter import *

size = 600
root = Tk()
canvas = Canvas(root, width = size, height = size)
canvas.pack()
count = 0
colors = ['blue', 'green', 'maroon', 'orange', 'pink', 'purple', 'red', 'yellow', 'violet','chartreuse', 'cyan2', 'orchid1']

while count < 1000:
    color = choice(colors)
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill = color)
    root.update()
    count += 1
