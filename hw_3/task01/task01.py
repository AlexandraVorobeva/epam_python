def cache(times: int):
    """
    This function accepts any function for cache
    and gives out cached value up to times number only.

    Args:
        times: number

    Returns:
        decorated function: callable

    """
    cacher = {}

    def wrapper(func):
        def func_cache(*args):
            if times > 0:
                if args in cacher and cacher[args][1] < times:
                    cacher[args][1] += 1
                    return cacher[args][0]
                else:
                    value = func(*args)
                    cacher[args] = [value, 0]
                    return value
            return func(*args)

        return func_cache

    return wrapper

