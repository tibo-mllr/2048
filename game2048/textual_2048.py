def read_player_command():
    move = input("Entrez votre commande :")
    if move not in ['g', 'd', 'h', 'b']:
        return read_player_command()
    return move


def read_size_grid():
    size = int(input("Entrez la taille du jeu :"))
    return size


def read_theme_grid():
    theme = input(
        "entrez le theme du jeu (Default : 0, Chemistry : 1, Alphabet : 2) :")
    if theme not in ['0', '1', '2']:
        return read_theme_grid()

    return theme
