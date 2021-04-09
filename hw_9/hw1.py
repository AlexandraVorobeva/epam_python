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

from typing import Iterator


def merge_sorted_files(file_list) -> Iterator:
    """
    This function merges integer from sorted files and returns an iterator.

    Args:
        file_list: path to file

    Returns: iterator (sorted values from merged files)

    >>> list(merge_sorted_files(["file1.txt"]))
    [1, 3, 5]
    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6]
    >>> list(merge_sorted_files(["file1.txt", "file2.txt", "file3.txt"]))
    [1, 2, 3, 4, 5, 5, 6, 7]

    """
    merged_list = []
    for file in file_list:
        with open(file, "r") as fl:
            for line in fl:
                merged_list.append(int(line.strip()))

    return (i for i in sorted(merged_list))