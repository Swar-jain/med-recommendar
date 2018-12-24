from Tkinter import *

class Program:

    def __init__(self):
        b = Button(text="click me", command=self.callback)
        b.pack()

    def callback(self):
        print "clicked!"

program = Program()

mainloop()
