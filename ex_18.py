def simmetr(s: int, i: int, j: int) -> bool:
    """
    Check if a substring is a palindrome using recursion.

    This function recursively checks whether the substring s[i:j+1] is a palindrome
    by comparing characters from both ends moving towards the center.

    Args:
        s (str): The string to check
        i (int): The starting index of the substring
        j (int): The ending index of the substring

    Returns:
        bool: True if the substring is a palindrome, False otherwise
    """
    if i >= j:
        return True

    elif s[i] != s[j]:
        return False

    else:
        return simmetr(s, i + 1, j - 1)


try:
    s = input("Введите строку для анализа: ")
    i = int(input("Введите начальный индекс: "))
    j = int(input("Введите конечный индекс: "))

    if not s:
        print("Ошибка! Строка не может быть пустой")

    elif i < 0 or j < 0:
        print("Ошибка! Индексы должны быть неотрицательными")

    elif i >= len(s) or j >= len(s):
        print(f"Ошибка! Индексы должны быть в диапазоне от 0 до {len(s)-1}")

    else:
        if i > j:
            i, j = j, i

        result = simmetr(s, i, j)
        print(f"Результат: {result}")

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
