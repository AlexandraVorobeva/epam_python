from typing import List

import pytest

from hw_1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -2, 3, 1, 4], 3, 8),
        ([1, 2, 3, 4], 2, 7),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    result = find_maximal_subarray_sum(nums, k)
    assert result == expected_result


def test_find_maximal_subarray_sum_raises():
    with pytest.raises(ValueError):
        find_maximal_subarray_sum([1, 3, 6, 7], 5)
