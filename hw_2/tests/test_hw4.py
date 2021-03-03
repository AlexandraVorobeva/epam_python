from unittest.mock import Mock

from hw_2.hw4 import cache


def test_cache():
    m = Mock()
    n = m
    m = cache(m)()
    m()
    m()
    assert n.call_count == 1