"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Supressor:
    """
    Сontext manager, that suppresses passed exception.
    """

    def __init__(self, exeption):
        self.exeption = exeption

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            yield
        except self.exc_type:
            pass


@contextmanager
def supressor(exeption):
    """
    Сontext manager, that suppresses passed exception.

    Args:
        exeption: any exeption
    """
    try:
        yield
    except exeption:
        pass

