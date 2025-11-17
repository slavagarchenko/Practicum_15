def mod(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    
    This function computes the GCD of two integers using recursion based on the Euclidean algorithm principle:
    gcd(a, b) = gcd(b, a mod b)

    Args:
        a (int): First number (non-negative integer)
        b (int): Second number (non-negative integer)

    Returns:
        int:     The greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return mod(b, a % b)
