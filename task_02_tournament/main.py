from typing import List


def display_result(participants_names):
    """
    Выводим список имён участников в первый день

    :param participants_names: список имён участников, например: ["Артемий", "Влад", "Дима", "Женя"]
    :type participants_names: List[str]
    """
    print(f"Первый день: {participants_names}")


def get_participants_names(names) -> List[str]:
    """
    Получаем элементы списка только с чётными индексами.

    :param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    :type names: List[str]

    :return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    :rtype: List[str]
    """
    return [names[name] for name in range(0, len(names), 2)]


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
