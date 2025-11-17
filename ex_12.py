from typing import Any


def search(a: list, x: Any) -> int:
    """
    Search for an element in a list using recursion.

    This function recursively checks if an element exists in a list.

    Args:
    a (list): The list to search through
    x: The element to search for

    Returns:
    int: 1 if the element is found, 0 if not found
    """
    if not a:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search(a[1:], x)


try:
    a = list(map(int, input("Введите список чисел: ").split()))
    x = int(input("Введите число для поиска: "))

    if not a:
        print("Ошибка! Список не может быть пустым")

    else:
        result = search(a, x)

        if result == 1:
            print(f"Число {x} найдено в списке")

        else:
            print(f"Число {x} не найдено в списке")

except ValueError:
    print("Ошибка! Введите числа через пробел")

except RecursionError:
    print("Ошибка! Слишком большие размеры вызвали переполнение стека")
