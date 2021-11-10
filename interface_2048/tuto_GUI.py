from tkinter import *
from pprint import pformat

<<<<<<< HEAD
def print_bonjour(i):
    label.config(text="Hello")

=======

def print_bonjour(i):
    label.config(text="Hello")


>>>>>>> e6c7b71895399f7c1b4be6944978bcf13a3d37e4
root = Tk()
frame = Frame(root, bg='white', height=100, width=400)
entry = Entry(root)
label = Label(root)

frame.grid(row=0, column=0)
entry.grid(row=1, column=0, sticky='ew')
label.grid(row=2, column=0)

frame.bind('<ButtonPress>', print_bonjour)
entry.bind('<KeyPress>', print_bonjour)
root.mainloop()
