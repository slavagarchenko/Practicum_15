def mod_number(a: int, b: int) -> int:
    """
    Calculate the modulus (remainder) of two numbers using recursion.

    This function computes the remainder when a is divided by b
    using the recursive principle of repeated subtraction.

    Args:
        a (int): The dividend (number to be divided).
        b (int): The divisor (number to divide by).

    Returns:
        int: The remainder when a is divided by b.
    """
    if a < b:
        return a
    else:
        return mod_number(a - b, b)


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    if b == 0:
        print("Ошибка! Деление на ноль невозможно")

    elif b < 0:
        print("Ошибка! Делитель должен быть положительным числом")

    else:
        result = mod_number(a, b)
        print(f"Остаток от деления {a} на {b}: {result}")

except ValueError:
    print("Ошибка! Введите целые числа")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
