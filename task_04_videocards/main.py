import random
from typing import List


def get_input_parameters():
    """
    Получаем список видеокарт

    :return: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    try:
        input_number = int(input("Кол-во видеокарт: "))
        if input_number <= 0:
            raise ValueError
        result = [random.randint(1000, 9999) for _ in range(input_number)]
        for i in range(1, input_number + 1):
            print(f"{i} Видеокарта: {result[i - 1]}")
        return result
    except ValueError:
        print("Введите только целочисленное положительное число.")
        get_input_parameters()


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт

    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print("\nСтарый список видеокарт: ", end="")
    for i in old_video_cards:
        print(i, end=" ")

    print("\nНовый список видеокарт: ", end="")
    for i in new_video_cards:
        print(i, end=" ")


def select_video_cards(video_cards: List[int]):
    """
    Удаляем из списка видеокарт наибольшие элементы.

    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]

    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    max_val = max(video_cards)
    copy_obj = video_cards.copy()
    [copy_obj.remove(max_val) for _ in range(copy_obj.count(max_val))]
    return copy_obj


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
