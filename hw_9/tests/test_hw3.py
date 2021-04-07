from pathlib import Path
from hw_9.hw3 import universal_file_counter


test_dir = Path.resolve(Path(__file__).parent)


def test_txt_counter():
    assert universal_file_counter(test_dir, "txt") == 6


def test_txt_counter_2():
    assert universal_file_counter(test_dir, "txt", str.split) == 14


def test_token_count():
    assert universal_file_counter(test_dir, "py") == 61
