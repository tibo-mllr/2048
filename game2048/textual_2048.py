def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    if move != "g" and move != "d" and move != "h" and move != "b":
        return read_player_command()
    else:
        return move

def read_size_grid():
    size = input ("entrez la taille du jeu")
    if size.type != int: 
        return read_size_grid
    else:
        return size

def read_theme_grid():
    theme = input ("entrez le theme du jeu")
    if theme not in ["Default" , "Chemistry", "Alphabet"]:
        return read_theme_grid
    else:
        return theme


