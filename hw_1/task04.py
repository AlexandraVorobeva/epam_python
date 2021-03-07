"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    This function computes how many tuples (i, j, k, l)
    there are such that A[i] + B[j] + C[k] + D[l] is zero.

    Args:
        a: list of integer values, a have same length of N where 0 ≤ N ≤ 1000
        b: list of integer values, b have same length of N where 0 ≤ N ≤ 1000
        c: list of integer values, c have same length of N where 0 ≤ N ≤ 1000
        d: list of integer values, d have same length of N where 0 ≤ N ≤ 1000

    Returns:
        int: value that counts how many tuples is zero
    """
    return len(
        [
            i + j + k + m
            for i in a
            for j in b
            for k in c
            for m in d
            if i + j + k + m == 0
        ]
    )
