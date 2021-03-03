"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence

import pytest


def check_fibonacci(data: Sequence[int]) -> bool:
    ans = False
    tmp1 = 0
    tmp2 = 1
    if not isinstance(data, Sequence):
        raise TypeError("Data is not Sequence")
    if len(data) == 0:
        return False
    while tmp1 < data[0]:
        tmp1, tmp2 = tmp2, tmp1 + tmp2
    if tmp1 == data[0]:
        for i in data:
            if i == tmp1:
                ans = True
            else:
                ans = False
                break
            tmp1, tmp2, = (
                tmp2,
                tmp1 + tmp2,
            )
    return ans


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([55, 89, 144], True),
        ([5], True),
        ([1, 8, 34], False),
        ([3, 4, 5], False),
        ([], False),
    ],
)
def test_check_fibonacci(value, expected_result: bool):
    result = check_fibonacci(value)
    assert result == expected_result


# def test_check_fibonacci_raises():
#    with pytest.raises(TypeError, match="Не тот тип данных"):
#        check_fibonacci(True)
