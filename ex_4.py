def sum_progress(a1, r, n):
    """
    """
    if n == 1:
        return a1
    else:
        return progress(a1, r, n) + sum_progress(a1, r, n - 1)
    
