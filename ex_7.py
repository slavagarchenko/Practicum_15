def mod(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

    This function computes the GCD of two integers using recursion based on the Euclidean algorithm principle:
    gcd(a, b) = gcd(b, a mod b)

    Args:
        a (int): First number (non-negative integer)
        b (int): Second number (non-negative integer)

    Returns:
        int: The greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return mod(b, a % b)


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    if a < 0 or b < 0:
        print("Ошибка! Оба числа должны быть неотрицательными")

    elif a == 0 and b == 0:
        print("Ошибка! НОД(0, 0) не определен")

    else:
        result = mod(a, b)
        print(f"НОД({a}, {b}) = {result}")

except ValueError:
    print("Ошибка! Введите целые числа")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
