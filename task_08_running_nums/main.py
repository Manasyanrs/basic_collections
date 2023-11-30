def get_input_parameters():
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    try:
        start_value = [1, 4, -3, 0, 10]
        input_number = int(input("Сдвиг: "))
        if input_number <= 0:
            raise ValueError
        print(f"Изначальный список: {start_value}")
        return [input_number, start_value]
    except ValueError:
        print("Введите только целочисленное положительное число.")
        get_input_parameters()


def display_result(shifted_list):
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    print(f"\nСдвинутый список: {shifted_list}")


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    return original_list[-shift:] + original_list[:-shift]


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
