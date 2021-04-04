import pytest
from hw_8.task1 import KeyValueStorage


def test_KeyValueStorage_brackets():
    actual_result = KeyValueStorage("task1.txt")
    assert actual_result["name"] == "kek"
    assert actual_result["last_name"] == "top"


def test_KeyValueStorage_dot():
    actual_result = KeyValueStorage("task1.txt")
    assert actual_result.name == "kek"
    assert actual_result.last_name == "top"


def test_KeyValueStorage_error():
    with pytest.raises(ValueError, match="Invalid key!"):
        KeyValueStorage("example.txt")
