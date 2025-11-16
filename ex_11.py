def ind_maxlist(a, index=0):
    """
    """
    if len(a) == 1:
        return index
    else:
        rest_index = ind_maxlist(a[1:], index + 1)
        return index if a[0] > a[rest_index - index] else rest_index
