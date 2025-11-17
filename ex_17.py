def function1(x, divisor=None):
    """
    Check if a number is prime using recursion.
    
    This function recursively determines whether a given number is prime
    by testing divisibility by increasing divisors.

    Args:
        x (int):                 The number to check for primality (positive integer)
        divisor (int, optional): The current divisor to test (starts at 2)

    Returns:
        int:                     1 if the number is prime, 0 if it is not prime
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
