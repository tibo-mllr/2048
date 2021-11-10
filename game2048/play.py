from grid_to_string import *
from grid_2048 import *
from textual_2048 import *
from random import *

def random_play(n):
    game_grid = init_game(n)
    print(grid_to_string(game_grid))
    D = ["up", "right", "down", "left"]
    while is_game_over(game_grid) == False:
        r=randint(0, 3)
        game_grid = move_grid(game_grid, D[r])
        game_grid = grid_add_new_tile(game_grid)
        print(grid_to_string(game_grid))

random_play(4)



