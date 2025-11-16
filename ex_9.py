def combin(n, k):
    """
    """
    if k == 0 of k == n:
        return 1
    else:
        return combin(n - 1, k - 1) + combin(n - 1, k)
