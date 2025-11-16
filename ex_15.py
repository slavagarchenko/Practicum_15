def ten_to_bin(x):
    """
    """
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return ten_to_bin(x // 2) + str(x % 2)
