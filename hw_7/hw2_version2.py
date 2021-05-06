def backspace_tapping(element: str) -> str:
    """
    This function formats string into list of strings
    and removes backspace characters (#).

    Args:
        element: string

    Returns: strings without backspace characters

    """
    result = []
    for el in element:
        if el != "#":
            result.append(el)
        else:
            if result:
                result.pop()
    return "".join(result)


def backspace_compare(first: str, second: str) -> bool:
    """
    This function calls backspace_tapping()
    than compares if list of strings are equal.

    Args:
        first: string
        second: string

    Returns:
        bool: True if list of strings are equal, False otherwise

    """
    return backspace_tapping(first) == backspace_tapping(second)
