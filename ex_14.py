def numbers(x: int) -> None:
    """
    Print the digits of a number in reverse order using recursion.
    
    This function recursively prints the digits of a positive integer
    from right to left (least significant digit to most significant digit).

    Args:
        x (int): The positive integer to process

    Returns:
        None
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)
