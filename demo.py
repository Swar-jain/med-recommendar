import Tkinter
root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Type your searching parameter!")
label.pack()
root.mainloop()

