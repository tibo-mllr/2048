from grid_2048 import *
from grid_to_string import *
from textual_2048 import *


def jeu(): #la fonction qui execute le jeu
    size = read_size_grid()
    theme = read_theme_grid()
    game_grid = init_game(size)
    while not is_game_over(game_grid):
        print(grid_to_string_with_size_and_theme(game_grid, theme, size))
        d = read_player_command()
        new_game_grid = move_grid(game_grid, d) #crée une grille new_game_grid égale a la grille de base si le deplacement entré par le joueur est pris en compte
        if not is_full_grid(new_game_grid) and game_grid != new_game_grid: #verifie que new_game_grid est bien différente de la grille de base et non pleine
            new_game_grid = grid_add_new_tile(new_game_grid) # si c'est le cas rajoute un 2 ou 4 dans une case vide

        game_grid = list(new_game_grid) #change notre grille de base par la nouvelle
    if is_game_winner(game_grid) or is_game_winner(new_game_grid): 
        print("Vous avez gané ^-^")

    else:
        print("Perdu : essayez encore...")

    Rep = input("Voulez-vous rejouer ? (1 : oui, 0 : non)") #demande si le joueur veut rejouer apres la fin du jeu

    if Rep == '1':
        jeu()


if __name__ == '__main__':
    print("Bienvenue")
    jeu()
