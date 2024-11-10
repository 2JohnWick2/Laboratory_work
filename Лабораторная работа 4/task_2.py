# TODO решите задачу
import json

INPUT_FILENAME = "input.json"

def task() -> float:
    # Считываем содержимое JSON файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Вычисляем сумму произведений "score" и "weight"
    total = sum(item["score"] * item["weight"] for item in data)

    # Округляем результат до 3 знаков после запятой
    return round(total, 3)

print(task())
