from pathlib import Path
from hw_9.hw3 import universal_file_counter

test_dir = Path().resolve().parent


def test_txt_counter():
    assert universal_file_counter(test_dir, "txt") == 8


def test_token_count():
    assert universal_file_counter(test_dir, "txt", str.split) == 8
