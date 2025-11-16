def mod_number(a, b):
    """
    """
    if a < b:
        return a
    else:
        return mod_number(a - b, b)
