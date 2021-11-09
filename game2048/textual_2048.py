def read_player_command():
    move = input("Entrez votre commande :")
    if move not in ['g', 'd', 'h', 'b']:
        return read_player_command()
    return move


def read_size_grid():
    size = int(input("Entrez la taille du jeu :"))
    return size


def read_theme_grid():
    theme = input("entrez le theme du jeu")
    if theme not in ["Default", "Chemistry", "Alphabet"]:
        return read_theme_grid()

    return theme
