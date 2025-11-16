def odd_list(a, n):
    """
    """
    if n == 0:
        return []
    else:
        rest = odd_list(a[1:], n - 1)
        if a[0] % 2 == 0:
            return [a[0]] + rest
        else:
            return rest
