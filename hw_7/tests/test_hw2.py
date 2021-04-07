import pytest

from hw_7.hw2 import backspace_compare


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("ab#c", "ad#c"),
        ("a##c", "#a#c"),
        ("", ""),
        ("##", "##"),
    ],
)
def test_backspace_compare_positive(first, second):
    assert backspace_compare(first, second) is True


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("a#c", "b"),
        ("c#", "#c"),
    ],
)
def test_backspace_compare_negative(first, second):
    assert backspace_compare(first, second) is False
