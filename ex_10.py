def maxlist(a):
    """
    """
    if len(a) == 1:
        return a[0]
    else:
        rest_max = maxlist(a[1:])
        return a[0] if a[0] > rest_max else return rest_max
