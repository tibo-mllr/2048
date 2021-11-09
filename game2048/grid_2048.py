from random import *


def create_grid(n):  #crée une grille de taille nxn
    game_grid = []

    for i in range(n):
        game_grid.append([' ' for j in range(n)])

    return game_grid


def grid_add_new_tile_at_position(game_grid, i, j):
    game_grid[i][j] = get_value_new_tile()
    return game_grid


def get_all_tiles(game_grid):
    L = []
    for l in game_grid:
        for e in l:
            if e == ' ':
                L.append(0)
            else:
                L.append(e)

    return L


def get_value_new_tile():
    L = [2, 4]
    return L[randint(0, 1)]


def get_empty_tiles_positions(game_grid):
    n = len(game_grid)
    E = []
    for i in range(n):
        for j in range(n):
            if game_grid[i][j] == ' ' or game_grid[i][j] == 0:
                E.append((i, j))

    return E


def get_new_position(game_grid):
    L = get_empty_tiles_positions(game_grid)
    n = len(L)
    return L[randint(0, n-1)]


def grid_get_value(game_grid, i, j):
    if game_grid[i][j] == ' ':
        return 0
    return game_grid[i][j]


def grid_add_new_tile(game_grid):
    (i, j) = get_new_position(game_grid)
    return grid_add_new_tile_at_position(game_grid, i, j)


def init_game(n):
    game_grid = create_grid(n)
    game_grid = grid_add_new_tile(game_grid)
    game_grid = grid_add_new_tile(game_grid)
    return game_grid
