from unittest.mock import Mock, call

import pytest

from hw_3.task01.task01 import cache


def test_cacher_decorator_without_caching():
    mock = Mock()

    def f(*args, **kwargs):
        return args, kwargs

    mock_f = mock(f)
    cached = cache(0)(mock_f)

    cached(1)
    cached(2)
    cached(2)

    actual_result = mock.mock_calls
    expected_result = [call(f), call()(1), call()(2), call()(2)]
    assert expected_result == actual_result


@pytest.mark.parametrize(
    ["first", "second"],
    [
        (1, 1),
        ["str", "str"],
        [True, True],
    ],
)
def test_cacher_decorator_check_outputs(first, second):
    @cache(2)
    def f(*args, **kwargs):
        return args, kwargs

    first = f(first)
    second = f(second)

    assert first is second

