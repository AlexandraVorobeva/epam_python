"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import List


def custom_range(sequence, *args) -> List[any]:
    """
    This function that accept any iterable of unique values and then it behaves as range function.

    Args:
        sequence: iterable object
        *args: items from iterable

    Returns:
        List: list from iterable

    """
    sl = slice(*args)
    if sl.start:
        start = sequence.index(sl.start)
    else:
        start = 0
    stop, step = sequence.index(sl.stop), sl.step or 1
    new_sequence = sequence[start:stop:step]
    return list(new_sequence)

