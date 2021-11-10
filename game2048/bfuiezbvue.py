import tkinter as tk

def graphical_grid_init():
    root = tk.Tk()
    root.title("2048")
    grillage = tk.Toplevel(root)
    grillage.grid()
    root.mainloop()

graphical_grid_init()