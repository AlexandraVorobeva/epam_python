from typing import List

import pytest

from hw_1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, -3, -3, -5, 1, -3, 1, 1, 5], 4, 4),
        ([1, 3, -1, -3, 5, 3, 6, 7], 1, 7),
        ([1, 3, 5, 7], 4, 16),
        ([1, 3, 5, 7], 7, 16),
        ([1, 3, 5, 7], 0, 0),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    result = find_maximal_subarray_sum(nums, k)
    assert result == expected_result

