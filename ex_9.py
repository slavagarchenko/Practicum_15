def combin(n: int, k: int) -> int:
    """
    Calculate the binomial coefficient C(n, k) using recursion.

    This function computes the number of ways to choose k items from n items
    without repetition and without regard to order (combinations).

    Parameters:
        n (int): Total number of items (non-negative integer)
        k (int): Number of items to choose (non-negative integer, 0 <= k <= n)

    Returns:
        int: The binomial coefficient C(n, k) - number of k-combinations from n elements
    """
    if k == 0 or k == n:
        return 1
    else:
        return combin(n - 1, k - 1) + combin(n - 1, k)


try:
    n = int(input("Введите общее число предметов: "))
    k = int(input("Введите число выбранных предметов: "))

    if n < 0 or k < 0:
        print("Ошибка! Оба числа должны быть неотрицательными")

    elif k > n:
        print("Ошибка! Число выбранных предметов не может быть больше общего числа")

    else:
        result = combin(n, k)
        print(f"C({n}, {k}) = {result}")

except ValueError:
    print("Ошибка! Введите целые числа")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
