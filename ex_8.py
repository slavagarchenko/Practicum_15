def fib(k: int) -> int:
    """
    Calculate the k-th Fibonacci number using recursion.

    This function computes the k-th number in the Fibonacci sequence,
    where each number is the sum of the two preceding ones.

    Args:
        k (int): The position in the Fibonacci sequence (non-negative integer).

    Returns:
        int: The k-th Fibonacci number.
    """
    if k <= 1:
        return k
    else:
        return fib(k - 1) + fib(k - 2)


try:
    k = int(input("Введите номер числа в последовательности Фибоначчи: "))

    if k < 0:
        print("Ошибка! Номер должен быть неотрицательным числом")

    else:
        result = fib(k)
        print(f"F({k}) = {result}")

except ValueError:
    print("Ошибка! Введите целое число")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
