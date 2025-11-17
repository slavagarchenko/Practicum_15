def prime(n, divisor):
    """
    Helper function to check if a number is prime using recursion.

    Args:
        n (int): The number to check
        divisor (int): The current divisor to test

    Returns:
        int: 1 if prime, 0 if not prime
    """
    if divisor * divisor > n:
        return 1

    if n % divisor == 0:
        return 0

    return prime(n, divisor + 1)


def function1(x: int) -> int:
    """
    Check if a number is prime using recursion.

    This function recursively determines whether a given number is prime
    by testing divisibility by increasing divisors.

    Args:
        x (int): The number to check for primality (positive integer)
        divisor (int, optional): The current divisor to test (starts at 2)

    Returns:
        int: 1 if the number is prime, 0 if it is not prime
    """
    if x < 2:
        return 0

    elif x == 2:
        return 1

    prime(x, 2)


try:
    x = int(input("Введите число: "))

    if x < 0:
        print("Ошибка! Число должно быть положительным")

    else:
        result = function1(x)

        if result == 1:
            print(f"Число {x} является простым")
        else:
            print(f"Число {x} не является простым")

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
