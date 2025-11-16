def simmetr(s, i, j):
    """
    """
    if i >= j:
        return True
    elif s[i] != s[j]:
        return False
    else:
        return simmetr(s, i + 1, j - 1)
