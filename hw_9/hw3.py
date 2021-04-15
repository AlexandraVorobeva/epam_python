"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    This function count lines in all files with that extension
    if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.

    Args:
        dir_path: path to directory
        file_extension:extension of files
        tokenizer: condition of the inputs

    Returns: integer (count of lines or tokens)

    """
    count = 0
    for file in dir_path.glob("*.{}".format(file_extension)):
        with open(file) as f:
            if tokenizer:
                for line in f.readlines():
                    count += len(tokenizer(line))
            else:
                count += sum(1 for _ in f.readlines())
    return count
