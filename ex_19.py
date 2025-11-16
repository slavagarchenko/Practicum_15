def count(a, b):
    """
    """
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return 1
    else:
        min_side = min(a, b)
        max_side = max(a, b)
        return 1 + count(min_side, max_side - min_side)
