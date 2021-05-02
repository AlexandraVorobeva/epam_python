"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""

import heapq
from typing import Generator, List


def unpacking(file_list: List[str]):
    """
    This function opens files and transforms content in integer.

    Args:
        file_list: list of paths to files

    Returns: generator of integers

    """
    for file in map(open, file_list):
        yield (int(line.strip()) for line in file)


def merge_sorted_files(file_list) -> Generator:
    """
    This function merges integer from sorted files and returns generator.

    Args:
        file_list: list of paths to files

    Returns: generator

    """
    merged_gen = (i for i in unpacking(file_list))
    yield from heapq.merge(*merged_gen)

