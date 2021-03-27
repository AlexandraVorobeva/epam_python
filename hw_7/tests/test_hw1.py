import pytest

from hw_7.hw1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ("element", "expected_result"),
    [
        ("RED", 6),
        ("lot", 1),
        ("A", 0),
        (["RED", "BLUE"], 1),
        ({"nested_key": "RED"}, 1),
    ],
)
def test_find_occurrences(element, expected_result: int):
    actual_result = find_occurrences(example_tree, element)

    assert actual_result == expected_result


second_tree = {
    "tuple": (0, "one"),
    "dict": {"tuple": (0, "one"), "another_tuple": (1, 2)},
    "list": [0, 1, {"abc": 3}, 1],
    "abc": 3,
}


@pytest.mark.parametrize(
    ("element", "expected_result"),
    [
        ((0, "one"), 2),
        (3, 2),
    ],
)
def test_find_occurrences_second_tree(element, expected_result: int):
    actual_result = find_occurrences(second_tree, element)

    assert actual_result == expected_result


boolean_tree = {"True": True, "False": False}


@pytest.mark.parametrize(
    ("element", "expected_result"),
    [
        (True, 1),
        (False, 1),
    ],
)
def test_find_occurrences_boolean_tree(element, expected_result: int):
    actual_result = find_occurrences(boolean_tree, element)

    assert actual_result == expected_result
