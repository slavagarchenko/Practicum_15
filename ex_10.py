from typing import Any

def maxlist(a: list) -> Any:
    """
    Find the maximum element in a list using recursion.
    
    This function recursively finds the largest value in a list by comparing
    the first element with the maximum of the rest of the list.

    Args:
        a (list): A list of comparable elements (numbers, strings, etc.)

    Returns:
        Any:      The maximum element in the list.
    """
    if len(a) == 1:
        return a[0]
    else:
        rest_max = maxlist(a[1:])
        return a[0] if a[0] > rest_max else rest_max
