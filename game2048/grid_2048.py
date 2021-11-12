from random import *


def create_grid(n):  # crée la grille vide de taille nxn et retourne cette grille la
    game_grid = []

    for i in range(n):
        game_grid.append([0 for j in range(n)])

    return game_grid


# renvoie la grille avec un nb aléatoire parmi {2,4} a la position i,j
def grid_add_new_tile_at_position(game_grid, i, j):
    game_grid[i][j] = get_value_new_tile()
    return game_grid


# renvoie une liste contenant toutes les valeurs de la grille en remplaçant les valeures vides par des 0
def get_all_tiles(game_grid):
    L = []
    for l in game_grid:
        for e in l:
            if e == ' ':
                L.append(0)
            else:
                L.append(e)

    return L


def get_value_new_tile():  # renvoie un nombre random parmi {2,4}
    L = [2, 4]
    return L[randint(0, 1)]


# renvoie une liste contenant les coordonnées des valeurs vides ou nulles de la grille
def get_empty_tiles_positions(game_grid):
    n = len(game_grid)
    E = []
    for i in range(n):
        for j in range(n):
            if game_grid[i][j] == ' ' or game_grid[i][j] == 0:
                E.append((i, j))

    return E


# retourne aléatoirement une des positions vides ou nulle
def get_new_position(game_grid):
    L = get_empty_tiles_positions(game_grid)
    n = len(L)
    return L[randint(0, n-1)]


# renvoie la valeure de l'élément dont les coordonnées sont mises en entrée et renvoie 0 si il n'ya rien dans cette case
def grid_get_value(game_grid, i, j):
    if game_grid[i][j] == ' ':
        return 0
    return game_grid[i][j]


# renvoie la grille avec une des positions nulles ou vides remplacée par un 2 ou 4
def grid_add_new_tile(game_grid):
    (i, j) = get_new_position(game_grid)
    return grid_add_new_tile_at_position(game_grid, i, j)


def init_game(n):  # cree une grille de taille n et remplace 2 cases par des 2 ou 4
    game_grid = create_grid(n)
    game_grid = grid_add_new_tile(game_grid)
    game_grid = grid_add_new_tile(game_grid)
    return game_grid


def move_row_left(game_row):  # deplacement a gauche sur une ligne
    n = len(game_row)
    i = 0
    row = list(game_row)
    while i < n-1:
        k = i + 1
        if row[i] == 0:
            while k < n-1 and row[k] == 0:
                k += 1

            row[i], row[k] = row[k], 0

        k = i + 1

        if row[i] != 0:
            while k < n-1 and row[k] == 0:
                k += 1

            if row[k] == row[i]:
                row[i] += row[k]
                row[k] = 0

        i += 1

    return row


def move_row_right(game_row):  # deplacement a droite sur une ligne
    rev = move_row_left(game_row[::-1])
    rev.reverse()

    return rev


def move_left(game_grid):  # deplacement a gauche sur l'ensemble de la grille
    for i in range(len(game_grid)):
        game_grid[i] = move_row_left(game_grid[i])
    return game_grid


def move_right(game_grid):  # deplacement a droite sur l'ensemble de la grille
    for i in range(len(game_grid)):
        game_grid[i] = move_row_right(game_grid[i])
    return game_grid


def move_up(game_grid):  # deplacement vers le haut sur l'ensemble de la grille
    T = [[] for i in range(len(game_grid))]
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            T[i].append(game_grid[j][i])

    T = move_left(T)

    TT = [[] for i in range(len(game_grid))]
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            TT[i].append(T[j][i])

    return TT


def move_down(game_grid):  # deplacement vers le bas de l'ensemble de la grille
    T = [[] for i in range(len(game_grid))]
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            T[i].append(game_grid[j][i])

    T = move_right(T)

    TT = [[] for i in range(len(game_grid))]
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            TT[i].append(T[j][i])

    return TT


def move_grid(game_grid, d):  # deplace de la grille vers la direction d indiquée en entrée
    if d == "h":
        return move_up(game_grid)
    if d == "b":
        return move_down(game_grid)
    if d == "g":
        return move_left(game_grid)
    if d == "d":
        return move_right(game_grid)


def is_grid_full(game_grid): #verifie si la grille est plein ou non 
    T = True
    for row in game_grid:
        if ' ' in row or 0 in row:
            T = False
    return T


def move_possible(game_grid): #verifie lesquels des mouvements apportent des changements a la grille
    T = [False, False, False, False]
    D = ["h", "d", "b", "g"]
    for i in range(len(D)):
        C = list(game_grid)
        res = list(move_grid(C, D[i]))
        if game_grid != res:
            T[i] = True

    return T


def is_game_over(game_grid): #retourne True si la grille est plein et il n'y a plus aucun mouvements possibles
    return is_grid_full(game_grid) and move_possible(game_grid) == [False, False, False, False]


def get_grid_tile_max(game_grid): #renvoie la plus grande valeur se trouvant sur la grille
    res = 0
    for i in range(len(game_grid)):
        for j in range(len(game_grid)):
            if grid_get_value(game_grid, i, j) > res:
                res = grid_get_value(game_grid, i, j)
    return res


def is_game_winner(game_grid): #renvoie True si la valeur 2048 a été atteinte
    if get_grid_tile_max(game_grid) >= 2048:
        return True

    return False
