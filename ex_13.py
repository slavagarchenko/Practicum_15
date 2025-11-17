def odd_list(a, n):
    """
    Extract the first n even numbers from a list using recursion.
    
    This function recursively processes a list and returns a new list containing
    the first n even numbers encountered in the original list.

    Parameters:
        a (list): The input list of integers to process
        n (int):  The maximum number of even numbers to extract

    Returns:
        list:     A list containing up to n even numbers from the original list
    """
    if n == 0:
        return []
    else:
        rest = odd_list(a[1:], n - 1)
        if a[0] % 2 == 0:
            return [a[0]] + rest
        else:
            return rest
