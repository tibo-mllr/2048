def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    L=['g','d','h','b']
    for i in range (len(L)):
        if move==L[i]:return move
    return "resaisez la commande"



def read_size_grid():
    size = int(input("Entrez la taille du jeu :"))
    return size

    


def read_theme_grid():
    theme = input("Choisissez le thème (Default, Chemistry, Alphabet) :")
    if theme not in ["Default", "Chemistry", "Alphabet"]:
        return read_theme_grid()

    return theme

    


