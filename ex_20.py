def comp(a, b, m, n):
    """
    Find the length of the longest common subsequence (LCS) between two strings using recursion.
    
    This function recursively calculates the length of the longest common subsequence
    between the first m characters of string a and the first n characters of string b.

    Args:
        a (str): The first string
        b (str): The second string
        m (int): The number of characters to consider from string a
        n (int): The number of characters to consider from string b

    Returns:
        int:     The length of the longest common subsequence
    """
    if m == 0 or n == 0:
        return 0
    elif a[m-1] == b[n-1]:
        return 1 + comp(a, b, m-1, n-1)
    else:
        return max(comp(a, b, m, n-1), comp(a, b, m-1, n))
