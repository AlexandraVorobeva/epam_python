import os

import pytest

from hw_4.task_1_read_file import read_magic_number


@pytest.fixture()
def file_name(text: str):
    filename = "file_with_number"
    with open(filename, "w") as f:
        f.write(text)
    yield filename
    os.remove(filename)


@pytest.mark.parametrize(
    ("text"),
    [
        ("1"),
        ("2"),
    ],
)
def test_read_magic_number(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is True


@pytest.mark.parametrize(
    ("text"),
    [
        ("5"),
        ("0"),
    ],
)
def test_read_magic_number_negative(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is False


@pytest.mark.parametrize(
    ("text"),
    [("Hello"), ("World!")],
)
def test_read_magic_number_value_error(file_name):
    with pytest.raises(ValueError, match="it must be a number"):
        read_magic_number(file_name)
