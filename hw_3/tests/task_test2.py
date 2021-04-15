import time

from hw_3.task02.task02 import fast_calculate


def test_fast_calculate():
    time_start = time.time()
    fast_calculate(500)
    time_finish = time.time()
    time_executing = time_finish - time_start
    assert time_executing <= 60