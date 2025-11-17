def numbers(x: int) -> None:
    """
    Print the digits of a number in reverse order using recursion.

    This function recursively prints the digits of a positive integer
    from right to left (least significant digit to most significant digit).

    Args:
        x (int): The positive integer to process

    Returns:
        None
    """
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


try:
    x = int(input("Введите число: "))

    if x < 0:
        print("Ошибка! Число должно быть положительным")

    elif x == 0:
        print("0")

    else:
        print(f"Цифры числа {x} в обратном порядке:")
        numbers(x)

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
