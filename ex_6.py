def degree5(n):
    """
    """
    if n == 1:
        return 0
    elif n % 5 != 0 or n < 5:
        return -1
    else:
        result = degree5(n//5)
        if result == -1:
            return result
        else:
            return 1 + result
