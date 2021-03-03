"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


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
