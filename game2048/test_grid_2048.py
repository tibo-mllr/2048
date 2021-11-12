from grid_2048 import *
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [
        ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


def test_grid_add_new_tile_at_position():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile_at_position(game_grid, 1, 1)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 4 in tiles


def test_get_value_new_tile():
    assert get_value_new_tile() in {2, 4}


def test_get_all_tiles():
    assert get_all_tiles([[' ', 4, 8, 2], [' ', ' ', ' ', ' '], [' ', 512, 32, 64], [
                         1024, 2048, 512, ' ']]) == [0, 4, 8, 2, 0, 0, 0, 0, 0, 512, 32, 64, 1024, 2048, 512, 0]
    assert get_all_tiles([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]) == [
        16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    assert get_all_tiles(create_grid(3)) == [0 for i in range(9)]


def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [
                                     512, 8, 16, 0]]) == [(0, 0), (0, 3), (1, 1), (3, 3)]
    assert get_empty_tiles_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [
                                     512, 8, 16, 0]]) == [(0, 0), (0, 3), (1, 1), (3, 3)]
    assert get_empty_tiles_positions(create_grid(2)) == [
        (0, 0), (0, 1), (1, 0), (1, 1)]
    assert get_empty_tiles_positions(
        [[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]) == []


def test_get_new_position():
    grid = [[0, 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]]
    x, y = get_new_position(grid)
    assert(grid_get_value(grid, x, y)) == 0
    grid = [[' ', 4, 8, 2], [' ', ' ', ' ', ' '], [
        ' ', 512, 32, 64], [1024, 2048, 512, ' ']]
    x, y = get_new_position(grid)
    assert(grid_get_value(grid, x, y)) == 0


def test_grid_add_new_tile():
    game_grid = create_grid(4)
    game_grid = grid_add_new_tile(game_grid)
    tiles = get_all_tiles(game_grid)
    assert 2 in tiles or 4 in tiles


def test_init_game():
    grid = init_game(4)
    tiles = get_all_tiles(grid)
    assert 2 in tiles or 4 in tiles
    assert len(get_empty_tiles_positions(grid)) == 14


def test_move_row_left():

    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]


def test_move_row_left():

    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]


def test_move_row_right():

    assert move_row_right([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right([4, 8, 16, 32]) == [4, 8, 16, 32]


def test_move_grid():
    assert move_grid([[2, 0, 0, 2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]], "left") == [
        [4, 0, 0, 0], [8, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0]]
    assert move_grid([[2, 0, 0, 2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]], "right") == [
        [0, 0, 0, 4], [0, 0, 0, 8], [0, 0, 0, 16], [0, 0, 0, 4]]
    assert move_grid([[2, 0, 0, 2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]], "up") == [
        [4, 8, 4, 2], [16, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_grid([[2, 0, 0, 2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]], "down") == [
        [0, 0, 0, 0], [0, 0, 0, 0], [4, 8, 0, 0], [16, 2, 4, 2]]


def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [
                         4, 8, 16, 32]]) == [True, True, True, True]
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [
                         16, 8, 4, 2]]) == [False, False, False, False]


def test_game_over():
    assert is_game_over([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [
                         16, 8, 4, 2]]) == True
    assert is_game_over([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [
                         4, 8, 16, 32]]) == False
    assert is_game_over([[2, 0, 0, 2], [2, 4, 0, 0], [
                        8, 4, 2, 0], [8, 2, 2, 0]]) == False


if __name__ == "__main__":
    test_create_grid()
    test_grid_add_new_tile_at_position()
    test_get_value_new_tile()
    test_get_all_tiles()
    test_get_empty_tiles_positions()
    test_get_new_position()
    test_grid_add_new_tile()
    test_init_game()
    test_move_row_left()
    test_move_row_right()
    test_move_grid()
    test_move_possible()
    test_game_over()
