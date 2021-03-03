from typing import List

import pytest

from hw_1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2, 3, 4], [2, 3, -3, 2], [-2, -4, -2, -4], [1, -1, 3, -2], 32),
        ([1, 2, 3, 4], [2, 3, 3, 2], [2, 4, 2, 4], [1, 1, 3, 2], 0),
        ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 256),
        ([0], [0], [0], [0], 1),
        ([], [], [], [], 0),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == expected_result
