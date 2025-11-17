def fib(k):
    """
    Calculate the k-th Fibonacci number using recursion.
    
    This function computes the k-th number in the Fibonacci sequence,
    where each number is the sum of the two preceding ones.

    Args:
        k (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int:     The k-th Fibonacci number.
    """
    if k <= 1:
        return k
    else:
        return fib(k - 1) + fib(k - 2)
