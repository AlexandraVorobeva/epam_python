"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    This function is generator that takes a number N as an input
    and returns a generator that yields N FizzBuzz numbers

    Args:
        n: int, number as an imput

    Returns: generator that yields N FizzBuzz numbers

    Instruction:
            - Install Python 3.8 (https://www.python.org/downloads/)
            - Install pytest `pip install pytest`
            - Clone the repository https://github.com/SparklingAcidity/epam_python
            - Checkout branch 4-hw
            - Open terminal
            - Run python hw_4/task_5_optional.py

    Examples:
            >>> list(fizzbuzz(5))
            ['1', '2', 'fizz', '4', 'buzz']
            >>> list(fizzbuzz(15))
            ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    """
    fizz = cycle(["", "", "fizz"])
    buzz = cycle(["", "", "", "", "buzz"])
    for i in range(1, n + 1):
        yield (next(fizz) + next(buzz)) or str(i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
