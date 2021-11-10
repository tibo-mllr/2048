from game2048.grid_2048 import *
import tkinter as tk
from tkinter import Canvas, ttk

Colours = {2: '#FBEEE6', 4: '#F2D7D5', 8: '#E6B0AA', 16: '#D98880', 32: '#CD6155', 64: '#C0392B',
           128: '#A93226', 256: '#922B21', 512: '#7B241C', 1024: '#641E16', 2048: '#512E5F', 4096: '#4A235A'}

game_grid = []


def key_pressed(event):
    global game_grid
    Dir = {'q': 'g', 'z': 'h', 'd': 'd', 's': 'b'}
    if not is_game_over(game_grid):
        new_game_grid = move_grid(list(game_grid), Dir[event.char])

        if not is_full_grid(new_game_grid) and game_grid != new_game_grid:
            new_game_grid = grid_add_new_tile(new_game_grid)

        game_grid = list(new_game_grid)
        display_and_update_graphical_grid(len(game_grid))

    else:
        if is_game_winner(game_grid):
            print("Vous avez gagné ! ^-^")
        else:
            print("Perdu, essayez encore...")

        Res = input("Voulez vous rejouer ?")
        if Res in ["Yes", "yes", "y", "1"]:
            size = input("Quelle taille ?")
            # theme = input("Et quel thème ? (Default, Chemistry, Alphabet)")
            graphical_grid_init(size)


def graphical_grid_init(n):
    global window
    window = tk.Tk()
    G_2048 = tk.Toplevel(window)
    G_2048.grid()

    Grid_size = tk.Label(window, text="Choose grid size")
    global Widgets
    Widgets = {}

    global Windows
    Windows = {}

    global background
    background = tk.Frame(G_2048)
    background.pack(fill=tk.BOTH, expand=True)

    global game_grid
    game_grid = init_game(n)
    create_pattern(n)
    display_and_update_graphical_grid(n)
    for i in range(n):
        for j in range(n):
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


def display_and_update_graphical_grid(n):

    for i in range(n):
        for j in range(n):
            if game_grid[j][i] != 0:
                Widgets[(i, j)].configure(text=game_grid[j][i])
                Widgets[(i, j)].configure(bg=Colours[game_grid[j][i]])
            else:
                Widgets[(i, j)].configure(text=' ')
                Widgets[(i, j)].configure(bg='#8B6C42')


if __name__ == '__main__':
    graphical_grid_init(4)
