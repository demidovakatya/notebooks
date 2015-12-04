# Works in Python 3.x
# This simple program might be useful to understand tkinter frames and widgets.

from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Buttons")
        self.pack(fill = BOTH, expand = True)
        self.var1 = BooleanVar() # for checkbox
        self.var2 = IntVar() # for scale

        frame1 = Frame(self)
        frame1.pack(fill = BOTH, expand = True)
        label = Label(frame1, text = "Hello")
        label.pack(side = LEFT, padx = 5, pady = 5)
        area = Entry(frame1) # creates textfield
        area.pack(padx = 5, expand = True)

        frame2 = Frame(self)
        frame2.pack(fill = BOTH, expand = True)
        cb = Checkbutton(frame2, text = "Show title", variable = self.var1, command = self.onClick)
        cb.select()
        cb.pack(side = LEFT)

        frame3 = Frame(self)
        frame3.pack(fill = BOTH, expand = True)
        scale = Scale(frame3, from_ = 0, to = 250, orient = HORIZONTAL, command = self.onScale)
        scale.pack(side = LEFT)
        labelScale = Label(frame3, text = 0, textvariable = self.var2)
        labelScale.pack(side = LEFT, padx = 30)


        closeButton = Button(self, text = "Close", command = self.quit) # creates a button
        closeButton.pack(side = RIGHT, padx = 5, pady = 5) 
        okButton = Button(self, text = "OK") # creates a useless button
        okButton.pack(side = RIGHT)

    def onClick(self):
        # toggles title of the window
        if self.var1.get() == True:
            self.master.title("Buttons")
        else:
            self.master.title("")

    def onScale(self, val):
        v = int(float(val))
        self.var2.set(v)

def main():
    root = Tk()
    root.geometry("250x300+30+30")
    app = Example(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  