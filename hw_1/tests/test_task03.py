from typing import Tuple

import pytest

from hw_1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        ("test1_find_max_min.txt", (-5, 34)),
        ("test2_find_max_min.txt", (1, 1)),
    ],
)
def test_maximum_and_minimum(file_name: str, expected_result: Tuple[int, int]):
    result = find_maximum_and_minimum(file_name)
    assert result == expected_result
