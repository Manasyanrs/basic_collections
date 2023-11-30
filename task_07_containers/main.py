def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    try:
        container = [[]]
        input_number = int(input("Кол-во контейнеров: "))
        if input_number <= 0:
            raise ValueError
        for iter_count in range(input_number):
            container_weight = int(input("Введите вес контейнера: "))
            if 0 >= container_weight > 200:
                raise ValueError
            else:
                container[0].append(container_weight)

        new_container_weight = int(input("Введите вес нового контейнера: "))
        if 0 >= new_container_weight > 200:
            raise ValueError
        else:
            container.append(new_container_weight)

        container[0].sort()
        container[0].reverse()
        return container

    except ValueError:
        print("Введите только целочисленное положительное число которое не большее 200.")
        get_input_parameters()


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    print(f"Номер, куда встанет новый контейнер: {serial_number_new_container}")


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """

    return len([index for index in list_container_weights if index >= new_container_weight]) + 1


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
