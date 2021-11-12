# Projet des Coding Weeks de l'équipe 4096

## Description
Notre équipe 4096 code le jeu 2048 dans le cadre des Coding Weeks.
Composée de 5 membres, cette équipe a clairement la meilleure ambiance

## Les 4096
* GESMIER Guillaume
* ISSAOUI Safae
* MULLER Thibault
* KOPP Bilal
* Vacherot Oscar

## Organisation
* Le fichier display_grid.py est la version finale : interface graphique avec menu. Les couleurs sont codées jusqu'à 8192 comme les thèmes donnés par l'énoncé. Tout marche (normalement) sauf pour rejouer : on est obligé de quitter les fenêtres et de relancer le code. Il prend en compte 'hdbg' comme demandé, mais aussi 'zqsd' et toutes ces lettres en majuscule par question de facilité.

* Les fichier play.py dans le dossier game2048 est le jeu fonctionnel sur python. Tout marche (normalement) même pour rejouer.

* Le dossier interface_2048 contient le fichiers portants sur l'interface tkinter, mais étant donné que pour display_grid.py il faut importer des fichiers d'autres dossiers, il a fallait le sortir et le mettre dans le dossier général.

* Le dossier game2048 contient tout les fichiers/modules nécessaires au bon fonctionnement du jeu, ainsi que les tests de ces fichiers. Tous les fichiers ont le nom précisé dans l'énoncé sauf :
    * move_row_left.py qui est une autre version de la fonction move_row_left définié dans grid_2048
    * move_row_right.py de même
    * play.py qui est décrit plus haut