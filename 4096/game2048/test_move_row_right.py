from game2048.move_row_right import move_row_right_vBilal
from move_row_left import move_row_left_vBilal
from move_row_right import move_row_right_vBilal

def test_move_row_right_vBilal():

    assert move_row_right_vBilal([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right_vBilal([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right_vBilal([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right_vBilal([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right_vBilal([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right_vBilal([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right_vBilal([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right_vBilal([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right_vBilal([4, 8, 16, 32]) == [4, 8, 16, 32]

test_move_row_right_vBilal()