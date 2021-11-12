from grid_2048 import *
from grid_to_string import *
from textual_2048 import *
import random as rd

def random_play():
    game_grid = init_game(4)
    D=['h','b','g','d']
    while not is_game_over(game_grid):
        r=rd.randint(0,3)
        game_grid = move_grid(game_grid, D[r])
        print(grid_to_string(game_grid))
        if not is_full_grid(game_grid):
            game_grid = grid_add_new_tile(game_grid)
    if is_game_winner(game_grid):
        print("Vous avez gagné ^-^")

    else:
        print("Perdu : essayez encore...")

random_play()

        

def jeu():
    size = read_size_grid()
    theme = read_theme_grid()
    game_grid = init_game(size)
    while not is_game_over(game_grid):
        print(grid_to_string_with_size_and_theme(game_grid, theme, size))
        d = read_player_command()
<<<<<<< HEAD
        game_grid = move_grid(game_grid, d)
        if not is_full_grid(game_grid):
            game_grid = grid_add_new_tile(game_grid)
    if is_game_winner(game_grid):
        print("Vous avez gagné ^-^")
=======
        new_game_grid = move_grid(game_grid, d)
        if not is_grid_full(new_game_grid) and game_grid != new_game_grid:
            new_game_grid = grid_add_new_tile(new_game_grid)

        game_griad = list(new_game_grid)
    if is_game_winner(game_grid) or is_game_winner(new_game_grid):
<<<<<<< HEAD
        print("Vous avez gané ^-^")
>>>>>>> e6c7b71895399f7c1b4be6944978bcf13a3d37e4
=======
        print("Vous avez gagné ^-^")
>>>>>>> Guillaume

    else:
        print("Perdu : essayez encore...")

    Rep = input("Voulez-vous rejouer ? (1 : oui, 0 : non)")

    if Rep == '1':
        jeu()


if __name__ == '__main__':
    print("Bienvenue")