"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    """
    This function accepts any function for cache and returns cached function.

    Args:
        func: any function for cache

    Returns:
        function: cached function

    """
    cacher = []

    def cache_func(*args):
        for safe_args, results in cacher:
            if safe_args == args:
                return results
        value = func(*args)
        cacher.append((args, value))
        return value

    return cache_func


