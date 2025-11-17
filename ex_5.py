def mod_number(a, b):
    """
    Calculate the modulus (remainder) of two numbers using recursion.
    
    This function computes the remainder when a is divided by b
    using the recursive principle of repeated subtraction.

    Args:
        a (int): The dividend (number to be divided).
        b (int): The divisor (number to divide by).

    Returns:
        int:     The remainder when a is divided by b.
    """
    if a < b:
        return a
    else:
        return mod_number(a - b, b)
