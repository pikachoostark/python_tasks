# Напишите программу, которая из JSON-структуры удаляет значения,
# являющиеся пустыми словарями ({}) или пустыми списками ([]), до тех пор, пока есть такие значения.
# Если удаляется значение в словаре, то удаляется и соответствующий ключ.
# Ограничение времени: 0,2 с, ограничение памяти: 6 Мб.
###
# Формат ввода:
# В единственной строке входных данных содержится строка длины n (1 ≤ n ≤ 1000).
# Гарантируется, что эта строка является правильной JSON-строкой.
#
# Формат вывода:
# Выведите через пробел количество удаленных пустых словарей и количество удаленных пустых списков.
import json
dict_counter, list_counter = 0, 0


def clean_struct(struct):
    global dict_counter, list_counter
    if isinstance(struct, dict):
        for key, value in struct.copy().items():
            cleaned_struct = clean_struct(value)
            if cleaned_struct is None:
                del struct[key]
            else:
                struct[key] = cleaned_struct
        if len(struct) == 0:
            dict_counter += 1
            return None
    if isinstance(struct, list):
        i = 0
        while i < len(struct):
            cleaned_struct = clean_struct(struct[i])
            if cleaned_struct is None:
                del struct[i]
            else:
                struct[i] = cleaned_struct
                i += 1
        if len(struct) == 0:
            list_counter += 1
            return None
    return struct


struct = json.loads(input())
clean_struct(struct)
print(dict_counter, list_counter)

# Решение:
# В задаче замаскирован обход дерева в глубину. Были участники, которые успешно решили задачу по-другому, например,
# с помощью регулярных выражений без преобразования строки в JSON.
# Полезно было знать о существовании модуля json, функции isinstance, знать, как работают словари и списки в Python.
# В решениях без преобразования строки в JSON разработчики часто старались удалять из строки последовательности
# вроде {}, [], но это нужно было делать аккуратно: например, в "{}, []" ничего удалять не нужно.
#
# Решение — при обходе дерева после просмотра поддерева удалять это поддерево, если оно пустое.
