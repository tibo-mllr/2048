from game2048.grid_2048 import *
import tkinter as tk
from tkinter import Canvas, StringVar, ttk
from functools import partial

Colours = {2: '#FBEEE6', 4: '#F2D7D5', 8: '#E6B0AA', 16: '#D98880', 32: '#CD6155', 64: '#C0392B',
           128: '#A93226', 256: '#922B21', 512: '#7B241C', 1024: '#641E16', 2048: '#512E5F', 4096: '#4A235A'}

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128",
                256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C",
                128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F",
                128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

game_grid = []

Entries = {}

def key_pressed(event):
    global game_grid
    Dir = {'q': 'g', 'z': 'h', 'd': 'd', 's': 'b'}
    if not is_game_over(game_grid):
        new_game_grid = move_grid(list(game_grid), Dir[event.char])

        if not is_full_grid(new_game_grid) and game_grid != new_game_grid:
            new_game_grid = grid_add_new_tile(new_game_grid)

        game_grid = list(new_game_grid)
        display_and_update_graphical_grid(len(game_grid), theme)

    else:
        if is_game_winner(game_grid):
            print("Vous avez gagné ! ^-^")
        else:
            print("Perdu, essayez encore...")


def graphical_grid_init():
    global window
    window = tk.Tk()
    global G_2048
    G_2048 = tk.Toplevel(window)
    G_2048.grid()

    Ent_Size = tk.StringVar("")
    Grid_size = tk.Label(window, text="Choose grid size")
    Grid_size.pack()

    Size_Entry = tk.Entry(window, textvariable=Ent_Size)
    Size_Entry.pack()

    Entries["Size"] = (Size_Entry, Ent_Size)

    Ent_Theme = tk.StringVar("")
    Grid_theme = tk.Label(
        window, text="Choisissez un thème : Default 0, Chemistry 1, Alphabet 2")
    Grid_theme.pack()

    Theme_Entry = tk.Entry(window, textvariable=Ent_Theme)
    Theme_Entry.pack()

    Entries["Theme"] = (Theme_Entry, Ent_Theme)

    Quit = tk.Button(window, text="Quit", command=quit)
    Quit.pack(side=tk.LEFT)

    Size = Ent_Size.get().strip()
    print("Size :", Size)
    Theme = Ent_Theme.get().strip()
    print("Theme :", Theme)
    Play = tk.Button(window, text="Play",
                    command=play)
    Play.pack(side=tk.RIGHT)
    global Widgets
    Widgets = {}

    global Windows
    Windows = {}

    global background
    background = tk.Frame(G_2048)
    background.pack(fill=tk.BOTH, expand=True)

    global game_grid
    window.mainloop()


def play(*args):
    size = Entries["Size"][1].get().strip()
    global game_grid
    game_grid = init_game(int(size))
    create_pattern(int(size))
    global theme
    theme = Entries["Theme"][1].get().strip()

    display_and_update_graphical_grid(int(size), theme)
    G_2048.bind('<KeyPress>', key_pressed)
    window.mainloop()


def create_pattern(n):
    C = tk.Canvas(background, bg='white', height=100*n, width=100*n)
    C.pack(fill=tk.BOTH, expand=True)

    # Lignes
    for i in range(n):
        C.create_line((0, 100*i), (100*n, 100*i), width=2)

    # Colonnes
    for i in range(n):
        C.create_line((100*i, 0), (100*i, 100*n), width=2)

    # Widgets

    for i in range(n):
        for j in range(n):
            Widgets[(i, j)] = tk.Label(background, bg='#8B6C42')
            Widgets[(i, j)].pack(fill=tk.BOTH, expand=True)
            Windows[(i, j)] = C.create_window(100*i + 50, 100 *
                                              j + 50, height=98, width=98, window=Widgets[(i, j)])


def display_and_update_graphical_grid(n, theme):

    for i in range(n):
        for j in range(n):
            if game_grid[j][i] != 0:
                Widgets[(i, j)].configure(text=THEMES[theme][game_grid[j][i]])
                Widgets[(i, j)].configure(bg=Colours[game_grid[j][i]])
            else:
                Widgets[(i, j)].configure(text=' ')
                Widgets[(i, j)].configure(bg='#8B6C42')

