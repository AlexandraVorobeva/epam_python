import pytest

from hw_7.hw3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    ("board", "expected_result"),
    [
        ([["x", "o", "-"], ["o", "x", "-"], ["-", "x", "x"]], "x wins!"),
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished!"),
        ([["o", "x", "-"], ["x", "o", "-"], ["-", "o", "o"]], "o wins!"),
        ([["x", "o", "o"], ["o", "x", "x"], ["x", "x", "o"]], "draw!"),
    ],
)
def test_tic_tac_toe_checker(board, expected_result):
    actual_result = tic_tac_toe_checker(board)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("board"),
    [
        ([["1", "1", "1"], ["2", "2", "2"], ["3", "3", "3"]]),
    ],
)
def test_tic_tac_toe_checker_error(board,):
    with pytest.raises(ValueError, match="Use only 'x', 'o', '-'  for game"):
        tic_tac_toe_checker(board)
