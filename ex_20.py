def comp(a, b, m, n):
    """
    """
    if m == 0 or n == 0:
        return 0
    elif a[m-1] == b[n-1]:
        return 1 + comp(a, b, m-1, n-1)
    else:
        return max(comp(a, b, m, n-1), comp(a, b, m-1, n))
