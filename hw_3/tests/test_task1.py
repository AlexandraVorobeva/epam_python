from io import StringIO

import pytest
from hw_3.task01.task01 import cache


@cache(times=1)
def f():
    return input("? ")


input_ = StringIO("first\n")


def test_cache(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", input_)
        first = f()
        second = f()
        third = f()
        assert first == second != third