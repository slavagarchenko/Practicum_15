def function1(x, divisor=None):
    """
    """
    if divisor is None:
        divisor = 2
    
    if x < 2:
        return 0
    elif x == 2:
        return 1
    elif divisor * divisor > x:
        return 1
    elif x % divisor == 0:
        return 0
    else:
        return function1(x, divisor + 1)
