import random


def get_input_parameters():
    """
    Получаем набор клеток

    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    try:
        input_number = int(input("Кол-во клеток: "))
        if input_number <= 0:
            raise ValueError
        result = [random.randint(0, input_number) for _ in range(input_number)]
        for i in range(1, input_number + 1):
            print(f"Эффективность {i} клетки: {result[i - 1]}")
        return result
    except ValueError:
        print("Введите только целочисленное положительное число.")
        get_input_parameters()


def display_result(cells):
    """
    Выводим список клеток у которых значение меньше индекса

    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    print("\nНеподходящие значения: ", end="")
    for i in cells:
        print(i, end=" ")


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.

    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]

    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    return [efficiency for i, efficiency in enumerate(cells, start=1) if efficiency < i]


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
