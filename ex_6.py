def degree5(n:int) -> int:
    """
    Calculate the exponent of the highest power of 5 that divides n.
    
    This function recursively determines the largest integer k such that 5^k divides n.
    In other words, it finds how many times n can be divided by 5 without leaving a remainder.

    Args:
        n (int): The number to analyze (positive integer).

    Returns:
        int:     The exponent k where 5^k divides n, or -1 if n is not a power of 5 
                or is not divisible by 5.
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
