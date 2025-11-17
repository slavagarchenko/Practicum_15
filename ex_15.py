def ten_to_bin(x: int) -> str:
    """
    Convert a decimal integer to its binary representation using recursion.

    This function recursively converts a positive decimal integer to a binary string
    by repeatedly dividing by 2 and building the binary representation from the remainders.

    Args:
        x (int): The decimal integer to convert (non-negative)

    Returns:
        str: The binary representation of the input number as a string
    """
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return ten_to_bin(x // 2) + str(x % 2)


try:
    x = int(input("Введите число для преобразования в двоичную систему: "))

    if x < 0:
        print("Ошибка! Число должно быть неотрицательным")

    else:
        result = ten_to_bin(x)
        print(f"Двоичное представление: {result}")

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
