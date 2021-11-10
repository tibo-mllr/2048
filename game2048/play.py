from game2048.grid_2048 import *
from game2048.grid_to_string import *
from game2048.textual_2048 import *


def jeu():
    size = read_size_grid()
    theme = read_theme_grid()
    game_grid = init_game(size)
    while not is_game_over(game_grid):
        print(grid_to_string_with_size_and_theme(game_grid, theme, size))
        d = read_player_command()
        game_grid = move_grid(game_grid, d)
        if not is_full_grid(game_grid):
            game_grid = grid_add_new_tile(game_grid)
    if is_game_winner(game_grid):
        print("Vous avez gané ^-^")

    else:
        print("Perdu : essayez encore...")

    Rep = input("Voulez-vous rejouer ? (1 : oui, 0 : non)")

    if Rep == '1':
        jeu()


if __name__ == '__main__':
    print("Bienvenue")
    jeu()
