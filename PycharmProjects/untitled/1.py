from tkinter import *

root = Tk()

one=Label(root, text="one",bg="red",fg="white")
one.pack()
two=Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three=Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT, fill=Y)

root.mainloop()

