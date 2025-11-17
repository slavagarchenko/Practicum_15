def ind_maxlist(a, index=0):
    """
    Find the index of the maximum element in a list using recursion.
    
    This function recursively finds the index of the largest value in a list
    by comparing elements while tracking the current index.

    Args:
        a (list):    A list of comparable elements (numbers, strings, etc.)
        index (int): The starting index (used internally for recursion, default 0)

    Returns:
        int:         The index of the maximum element in the list.
    """
    if len(a) == 1:
        return index
    else:
        rest_index = ind_maxlist(a[1:], index + 1)
        return index if a[0] > a[rest_index] else rest_index
