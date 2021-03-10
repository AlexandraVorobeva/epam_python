"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    This function finds 10 longest words consisting from largest amount of unique symbols.

    Args:
        file_path: path to working file

    Returns:
        str: list of 10 longest words

    """
    count_dictionary = {}
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            clean_line = line.translate(str.maketrans("", "", string.punctuation)).split()
            for word in clean_line:
                count_dictionary[word] = len(set(word))
        result_list = [i[0] for i in sorted(count_dictionary.items(), reverse=True, key=lambda a: a[1])[:10]]
        return result_list



def get_rarest_char(file_path: str) -> str:
    """
    This function finds rarest symbol for document.

    Args:
        file_path: path to working file

    Returns:
          str: string of rarest symbol

    """
    count_dictionary = {}
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            clean_line = line.translate(str.maketrans("", "", string.punctuation))
            for char in clean_line:
                if char in count_dictionary:
                    count_dictionary[char] += 1
                else:
                    count_dictionary[char] = 1
        result_list = sorted(count_dictionary.items(), key=lambda item: item[1])
        result_string = [char[0] for char in result_list if char[1] == result_list[0][1]]
        return " ".join(result_string)


def count_punctuation_chars(file_path: str) -> int:
    """
    This function counts every punctuation char.

    Args:
        file_path: path to working file

    Returns:
        int: count of punctuation char

    """
    with open(file_path, encoding="unicode-escape") as text:
        res = 0
        for line in text:
            res += len([char for char in line if char in string.punctuation])
        return res


def count_non_ascii_chars(file_path: str) -> int:
    """
    This function counts every non ascii char.

    Args:
        file_path: path to working file

    Returns:
        int: count of non ascii chars

    """
    with open(file_path, encoding="unicode-escape") as text:
        res = 0
        for line in text:
            res += len([char for char in line if not char.isascii()])
        return res


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    This function finds most common non ascii char for document.

    Args:
        file_path: path to working file

    Returns:
        str: the most common non ascii char

    """
    count_dictionary = {}
    with open(file_path, encoding="unicode-escape") as text:
        for line in text:
            for char in line:
                if not char.isascii() and char != " ":
                    if char in count_dictionary:
                        count_dictionary[char] += 1
                    else:
                        count_dictionary[char] = 1
    result_list = sorted(count_dictionary.items(), reverse=True, key=lambda item: item[1])
    result_string = [char[0] for char in result_list if char[1] == result_list[0][1]]
    return " ".join(result_string)