"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    This function returns the max sum of this sub-array.

    Args:
        nums: list of integers numbers
        k: length of sub-array

    Returns:
        int: maximal sum of sub-array
    """
    max_sum_sub = 0
    if len(nums) < k:
        k = len(nums)
    for i in range(len(nums) - k + 1):
        cur_sum_sub = 0
        for j in range(k):
            cur_sum_sub += nums[i + j]
            if cur_sum_sub > max_sum_sub:
                max_sum_sub = cur_sum_sub
    return max_sum_sub
