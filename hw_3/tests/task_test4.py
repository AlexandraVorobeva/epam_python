import pytest

from hw_3.task04.task04 import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"], [(9, True), (153, True), (154, False), (int(), True)]
)
def test_is_armstrong(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result

