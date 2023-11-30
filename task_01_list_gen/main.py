from typing import List


def get_input_parameters() -> int:
    """
    Получаем N

    :return: N, например: 14
    :rtype: int
    """
    try:
        input_number = int(input("Введите число: "))
        if input_number <= 0:
            raise ValueError
        return input_number
    except ValueError:
        print("Введите только целочисленное положительное число.")
        get_input_parameters()


def display_result(odd_numbers):
    """
    Выводим список нечётных чисел

    :param odd_numbers: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :type odd_numbers: List[int]
    """
    print(f"Список из нечётных чисел от 1 до N: {odd_numbers}")


def get_odd_numbers(number) -> List[int]:
    """
    Получаем отсортированный по возрастанию список
    нечётных чисел от 1 до number.

    :param number: до какого числа нужно рассчитать, например: 14
    :type number: int

    :return: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :rtype: List[int]
    """
    return [num for num in range(1, number + 1, 2)]


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
