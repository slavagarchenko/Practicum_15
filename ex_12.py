def search(a, x):
    """
    """
    if not a:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search (a[1:], x)
