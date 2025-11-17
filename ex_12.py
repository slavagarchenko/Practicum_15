from typing import Any

def search(a: list, x: Any) -> int:
    """
    Search for an element in a list using recursion.
    
    This function recursively checks if an element exists in a list.

    Args:
    a (list): The list to search through
    x: The element to search for

    Returns:
    int: 1 if the element is found, 0 if not found
    """
    if not a:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search(a[1:], x)
