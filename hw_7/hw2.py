"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest
from typing import List


def backspace_tapping(element: str) -> List[str]:
    """
    This function formats string into list of strings
    and removes backspace characters (#).

    Args:
        element: string

    Returns: List of strings

    """
    return [
        el
        for el, next_el in zip_longest(element, element[1:])
        if el != "#" and next_el != "#"
    ]


def backspace_compare(first: str, second: str) -> bool:
    """
    This function calls backspace_tapping()
    than compares if list of strings are equal.

    Args:
        first: string
        second: string

    Returns:
        bool: True if list of strings are equal, False otherwise

    """
    return backspace_tapping(first) == backspace_tapping(second)
