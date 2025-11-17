def odd_list(a: list, n: int) -> list:
    """
    Extract the first n even numbers from a list using recursion.

    This function recursively processes a list and returns a new list containing
    the first n even numbers encountered in the original list.

    Args:
        a (list): The input list of integers to process
        n (int): The lenth of this list

    Returns:
        list: A list containing up to n even numbers from the original list
    """
    if not a:
        return []

    result = odd_list(a[1:])

    if a[0] % 2 == 0:
        return [a[0]] + result
    else:
        return result


try:
    a = list(map(int, input("Введите список чисел: ").split()))

    if not a:
        print("Ошибка! Список не может быть пустым")

    else:
        n = len(a)

        result = odd_list(a, n)

        if len(result) == 0:
            print("(В списке нет четных чисел)")
        else:
            print(f"Четные числа: {result}")

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
