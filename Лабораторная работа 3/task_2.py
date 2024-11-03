# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, delimiter=','):
    participants_1 = str_1.split(delimiter)  # Разделяем строки на списки участников, используя указанный разделитель
    participants_2 = str_2.split(delimiter)
    common_participants = list(set(participants_1).intersection(participants_2)) # Находим пересечение двух множеств участников и формируем список
    common_participants.sort() # Сортируем список по алфавиту
    return common_participants # Возвращаем отсортированный список общих участников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
# Проверка работы функции с разделителем '|'
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, delimiter='|'))