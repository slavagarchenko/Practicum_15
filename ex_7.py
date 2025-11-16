def mod(a, b):
    """
    """
    if b == 0:
        return a
    else:
        return mod(b, a % b)
