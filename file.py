from Tkinter import *
root = Tk()
def save():
    open("text.txt","w").close()
    text = e.get() + "\n" + e1.get() + "\n" +  e2.get() + "\n"
    with open("text.txt", "a") as f:
        f.write(text)
w1 = Label(root, text="Controller value")
w1.pack()
e = Entry(root)
e.pack()
w2 = Label(root, text="Velocity")
w2.pack()
e1 = Entry(root)
e1.pack()
w3 = Label(root, text="Desired Heading")
w3.pack()
e2 = Entry(root)
e2.pack()
toolbar = Frame(root)
b = Button(toolbar, text="save", width=9, command=save)
b.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
mainloop()
