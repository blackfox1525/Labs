# TODO решите задачу
import json


def task(file) -> float:
    """
    Читает JSON файл, вычисляет сумму произведений "score" и "weight"
    для каждого словаря, и возвращает округленный результат.
    """
    with open(file, 'r') as file:
        data = json.load(file)  # Загружаем данные из JSON

        # Вычисляем сумму произведений
        total = sum(entry['score'] * entry['weight'] for entry in data)

    # Возвращаем результат с округлением до 3 знаков
    return round(total, 3)


# Используем загруженный файл
file_path = "input.json"  # Путь к загруженному файлу

print(task(file_path))
