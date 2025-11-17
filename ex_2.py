def count(n: int) -> int:
    """
    Count the number of digits in a given integer using recursion.

    This function calculates the number of digits in a non-negative integer
    by recursively dividing the number by 10 until it becomes less than 10.

    Args:
        n (int): A non-negative integer whose digits are to be counted.

    Returns:
        int: The number of digits in the given integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)


try:
    n = int(input("Введите натуральное число: "))

    if n < 0:
        print("Ошибка: Число должно быть натуральным (неотрицательным)")

    else:
        result = count(n)
        print(f"Количество цифр в числе {n}: {result}")

except ValueError:
    print("Ошибка! Введите целое число")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
