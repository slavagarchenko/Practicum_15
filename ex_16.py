def ten_to_n(x, n):
    """
    """
    if x == 0:
        return ""
        
    digits = "0123456789ABCDEF"
    reminder = x % n
    quotient = x // n
    
    if quotient == 0:
        return digits[remainder]
    else:
        return ten_to_n(quotien, n) + digits[remainder]

def ten_to_n_full(x, n):
    """
    """
    if x == 0:
        return "0"
    return ten_to_n(x, n)
