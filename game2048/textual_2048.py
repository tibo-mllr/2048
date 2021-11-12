def read_player_command(): #lis et retourne la commande rentrée par le joueur
    move = input("Entrez votre commande :")
    if move not in ['g', 'd', 'h', 'b']:
        return read_player_command()
    return move


def read_size_grid(): #lis et retourne la taille de grille rentrée par le joueur
    size = int(input("Entrez la taille du jeu :"))
    return size


def read_theme_grid(): #lis et retourne le thème rentré par le joueur
    theme = input(
        "entrez le theme du jeu (Default : 0, Chemistry : 1, Alphabet : 2) :")
    if theme not in ['0', '1', '2']:
        return read_theme_grid()

    return theme
