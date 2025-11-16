def progress(a1, r, n):
    """
    """
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)
