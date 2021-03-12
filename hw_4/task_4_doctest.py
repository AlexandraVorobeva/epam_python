"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function takes a number N as an input and returns N FizzBuzz numbers.

    Args:
        n: number, sequence length

    Returns:
        List: FizzBuzz sequence

    Instruction:
            - Install Python 3.8 (https://www.python.org/downloads/)
            - Install pytest `pip install pytest`
            - Clone the repository https://github.com/SparklingAcidity/epam_python
            - Checkout branch 4-hw
            - Open terminal
            - Run python hw_4/task_4_doctest.py
    Examples:
            >>> fizzbuzz(5)
            ['1', '2', 'Fizz', '4', 'Buzz']
            >>> fizzbuzz(15)
            ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']
            >>> fizzbuzz(0)
            Traceback (most recent call last):
            ...
            ValueError: n must be > 0
            >>> fizzbuzz(-5)
            Traceback (most recent call last):
            ...
            ValueError: n must be > 0


    """
    if n < 1:
        raise ValueError("n must be > 0")
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("Fizz Buzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
