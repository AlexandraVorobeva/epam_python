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
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    def get_value_from_file(path: str) -> int:
        with open(path) as f:
            for line in f:
                yield int(line)

    def get_next_from_iterator(iterator: Generator) -> Optional[int]:
        try:
            value = next(iterator)
        except StopIteration:
            value = None
        return value  # noqa

    def merge_sorted_files(file_list: List[str]) -> Iterator:

        first_arr = get_value_from_file(file_list[0])
        second_arr = get_value_from_file(file_list[1])
        first = next(first_arr)
        second = next(second_arr)

        while True:
            if second is None:
                yield first
                first = get_next_from_iterator(first_arr)

            elif first is None:
                yield second
                second = get_next_from_iterator(second_arr)

            elif first < second:
                yield first
                first = get_next_from_iterator(first_arr)
            else:
                yield second
                second = get_next_from_iterator(second_arr)