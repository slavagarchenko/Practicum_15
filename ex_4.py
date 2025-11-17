def sum_progress(a1, r, n):
    """
    Calculate the sum of the first n terms of a geometric progression.
    
    Parameters:
    a1 (float): The first term of the geometric progression.
    r (float):  The common ratio of the geometric progression.
    n (int):    The number of terms to sum.
    
    Returns:
    float:      The sum of the first n terms of the geometric progression.
    """
    if n == 1:
        return a1
    else:
        return progress(a1, r, n) + sum_progress(a1, r, n - 1)
