"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def check_line(*el) -> bool:
    """
    This function checks that all elements in list are equal.

    Args:
        *el: list

    Returns:
        bool: True if elements are equal, False otherwise

    """
    return len(set(el)) == 1


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    This function checks if the are some winners in Tic-Tac-Toe (board 3x#).

    Args:
        board: list of list

    Returns:
        string: if there is "x" winner, return "x wins!"
        "o" winner,  return "o wins!"
        if there is a draw, d return "draw!"
        if board is unfinished, return "unfinished!"

    """
    #check value
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["x", "o", '-']:
                raise ValueError("Use only 'x', 'o', '-'  for game")

    # check horizontal and vertical
    for i in range(3):
        horizontal = check_line(*board[i])
        vertical = check_line(board[0][i], board[1][i], board[2][i])
        if horizontal or vertical:
            return f"{str(board[i][i])} wins!"

    #check diagonals
    diag_1 = check_line(*[board[i][i] for i in range(3)])
    diag_2 = check_line(*[board[2 - i][i] for i in range(3)])
    if diag_1 or diag_2:
        return f"{str(board[1][1])} wins!"

    #check if it draw
    if sum(board[i].count("-") for i in range(3)) == 0:
        return "draw!"
    else:
        return "unfinished!"

