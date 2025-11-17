def simmetr(s, i, j):
    """
    Check if a substring is a palindrome using recursion.
    
    This function recursively checks whether the substring s[i:j+1] is a palindrome
    by comparing characters from both ends moving towards the center.

    Parameters:
        s (str): The string to check
        i (int): The starting index of the substring
        j (int): The ending index of the substring

    Returns:
        bool:    True if the substring is a palindrome, False otherwise
    """
    if i >= j:
        return True
    elif s[i] != s[j]:
        return False
    else:
        return simmetr(s, i + 1, j - 1)
