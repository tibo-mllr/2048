from grid_2048 import *
from grid_to_string import *
from textual_2048 import *
import random as rd

def random_play():
    game_grid = init_game(4)
    D=["g", "d" , "h" , "b"]
    while not is_game_over(game_grid):
        print(grid_to_string_with_size(game_grid, 4))
        r=rd.randint(0,3)
        new_game_grid = move_grid(game_grid, D[r])
       
<<<<<<< HEAD
        if not is_full_grid(new_game_grid):
=======
        if not is_grid_full(new_game_grid):
>>>>>>> Guillaume
            new_game_grid = grid_add_new_tile(new_game_grid)
        
        game_grid = list(new_game_grid)
    if is_game_winner(game_grid) or is_game_winner(new_game_grid):
        print("Vous avez gagné ^-^")

    else:
        print("Perdu : essayez encore...")

if __name__ == "__main__":
    random_play()