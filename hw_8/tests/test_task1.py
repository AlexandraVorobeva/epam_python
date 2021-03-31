import pytest
from hw_8.task1 import KeyValueStorage


@pytest.fixture()
def file_name(data: str):
    filename = "example.txt"
    with open(filename, "w") as fl:
        fl.write(data)
    yield filename


@pytest.mark.parametrize(
    ("data"),
    [
        ("1=something"),
        ("1=1"),
        ("Hello!=world!"),
        ("return=return"),
    ],
)
def test_value_error(file_name):
    with pytest.raises(ValueError, match="Incorrect key!"):
        KeyValueStorage(file_name)


@pytest.mark.parametrize(
    ("data", "correct_storage"),
    [
        (
            "name=kek last_name=top power=9001 song=shadilay",
            {"name": "kek", "last_name": "top", "power": 9001, "song": "shadilay"},
        ),
        ("name=kek name=run", {"name": "kek"}),
    ],
)
def test_key_value_storage(file_name, correct_storage):
    storage = KeyValueStorage(file_name)
    assert storage["name"] == storage.name == correct_storage["name"]
