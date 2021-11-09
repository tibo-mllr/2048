from grid_2048 import *

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128",
                256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C",
                128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F",
                128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def grid_to_string(game_grid, n):
    Max = long_value(game_grid)
    L = """"""
    for i in range(n):
        # Ligne déco 1
        for j in range(n):
            L += """ """
            for k in range(Max + 2):
                L += """="""
            L += """ """
        L += """
"""

        # Ligne nombres
        for j in range(n):
            L += """| """
            value = grid_get_value(game_grid, i, j)

            if value != 0:
                print("OK1")
                long = len(str(value))
                vide = Max - long
                for k in range(vide // 2):
                    print("OK2")
                    L += """ """

                L += str(value)

                for k in range(vide // 2 + 1):
                    print("OK3")
                    L += """ """

            else:
                for k in range(Max):
                    L += """ """
            L += """ |"""
        L += """
"""

        # Ligne déco 2
        for j in range(n):
            L += """ """
            for k in range(Max + 2):
                L += """="""
            L += """ """

        L += """
"""

    return L


# La vrai fonction

def grid_to_string_with_size(game_grid, n):
    L = """"""
    l = len(game_grid)
    for i in range(l):
        # Ligne déco 1
        for j in range(l):
            L += """ """
            for k in range(n):
                L += """="""
            L += """ """
        L += """
"""

        # Ligne nombres
        for j in range(l):
            L += """| """
            value = grid_get_value(game_grid, i, j)
            if value != 0:
                L += str(value)
            else:
                for k in range(n - 2):
                    L += """ """
            L += """ |"""
        L += """
"""

        # Ligne déco 2
        for j in range(l):
            L += """ """
            for k in range(n):
                L += """="""
            L += """ """

        L += """
"""

    return L


def long_value(grid):
    i = 0
    n = len(grid)
    for j in range(n):
        for k in range(n):
            if i < len(str(grid[j][k])):
                i = len(str(grid[j][k]))
    return i


def long_value_with_theme(game_grid, theme):
    return """ """


def grid_to_string_with_size_and_theme(game_grid, theme, n):
    return """ """
