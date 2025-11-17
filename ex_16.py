def ten_to_n(x: int, n: int) -> str:
    """
    Convert a decimal integer to its representation in base n using recursion.
    
    This function recursively converts a positive decimal integer to a string
    representation in the given base by repeatedly dividing by n and building
    the representation from the remainders.

    Args:
        x (int): The decimal integer to convert (positive)
        n (int): The target base (2 to 16)

    Returns:
        str:     The representation of the input number in base n as a string
    """
    if x == 0:
        return ""
        
    digits = "0123456789ABCDEF"
    remainder = x % n
    quotient = x // n
    
    if quotient == 0:
        return digits[remainder]
    else:
        return ten_to_n(quotient, n) + digits[remainder]


def ten_to_n_full(x: int, n: int) -> str:
    """
    Convert a decimal integer to its representation in base n (complete version).
    
    This is a wrapper function that handles the special case of zero and
    provides complete base conversion for all non-negative integers.

    Args:
        x (int): The decimal integer to convert (non-negative)
        n (int): The target base (2 to 16)

    Returns:
        str:     The representation of the input number in base n as a string
    """
    if x == 0:
        return "0"
    return ten_to_n(x, n)
