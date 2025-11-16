def fib(k):
    """
    """
    if k <= 1:
        return k
    else:
        return fib(k - 1) + fib(k - 2)
