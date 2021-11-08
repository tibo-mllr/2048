from grid_2048 import create_grid
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [
        ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]


if __name__ == "__main__":
    test_create_grid()
