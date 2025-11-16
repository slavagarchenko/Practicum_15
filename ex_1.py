def pownum(a: int | float, n: int) -> int | float:
    """
    Calculate the power of a number using recursion.
    
    This function computes the result of raising base 'a' to the exponent 'n'
    using a recursive approach.
    
    Args:
        a (int or float): The base number to be raised to the power
        n (int):          The exponent (non-negative integer)
    
    Returns:
        int or float:     The result of a raised to the power of n (a^n)
    """
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * pownum(a, n - 1)
