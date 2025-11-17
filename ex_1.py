def pownum(a: float, n: int) -> float:
    """
    Calculate the power of a number using recursion.

    This function computes the result of raising base 'a' to the exponent 'n'
    using a recursive approach.

    Args:
        a (float): The base number to be raised to the power
        n (int): The exponent (non-negative integer)

    Returns:
        float: The result of a raised to the power of n (a^n)
    """
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * pownum(a, n - 1)


try:
    a = float(input("Введите число для возведения в степень: "))
    n = int(input("Введите степень числа: "))

    if n < 0:
        print("Ошибка! Степень должна быть неотрицательной.")

    elif a == 0 and n == 0:
        print("0^0 математически неопределено")

    else:
        result = pownum(a, n)
        print(f"Результат: {result}")

except ValueError:
    print("Ошибка ввода! Убедитесь, что введены корректные данные")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
