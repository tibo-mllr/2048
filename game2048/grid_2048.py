def create_grid(n):
    game_grid = []

    for i in range(n):
        game_grid.append([' ' for j in range(n)])

    return game_grid
