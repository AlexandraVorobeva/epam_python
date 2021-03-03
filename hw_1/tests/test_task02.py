from typing import Sequence

import pytest

from hw_1.task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([55, 89, 144], True),
        ([5], True),
        ([1, 8, 34], False),
        ([3, 4, 5], False),
        ([], False),
    ],
)
def test_check_fibonacci(value, expected_result: bool):
    result = check_fibonacci(value)
    assert result == expected_result
