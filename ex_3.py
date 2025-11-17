def progress(a1: float, r: float, n: int) -> float:
    """
    Calculate the n-th term of a geometric progression using recursion.

    This function computes the n-th term of a geometric progression
    using the recursive formula: a_n = r + a_{n-1}

    Args:
        a1 (float): The first term of the geometric progression.
        r (float): The common ratio of the geometric progression.
        n (int): The term number to calculate (positive integer).

    Returns:
        float: The value of the n-th term in the geometric progression.
    """
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)


try:
    a1 = float(input("Введите первый член арифметической прогрессии: "))
    r = float(input("Введите разность арифметической прогрессии: "))
    n = int(input("Введите номер элемента, который нужно найти: "))

    if n <= 0:
        print("Ошибка! Номер элемента должен быть положительным числом")

    else:
        result = progress(a1, r, n)
        print(f"{n}-й член арифметической прогрессии: {result}")

except ValueError:
    print("Ошибка! Введите корректные числа")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
