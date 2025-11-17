def count(a, b):
    """
    Count the number of squares that can be cut from a rectangle using recursion.
    
    This function calculates how many squares of the largest possible size can be cut
    from an a x b rectangle using a greedy algorithm. At each step, it cuts the largest
    possible square from the remaining rectangle.

    Args:
        a (int): The length of the rectangle (positive integer)
        b (int): The width of the rectangle (positive integer)

    Returns:
        int:     The total number of squares that can be cut from the rectangle
    """
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return 1
    else:
        min_side = min(a, b)
        max_side = max(a, b)
        return 1 + count(min_side, max_side - min_side)
