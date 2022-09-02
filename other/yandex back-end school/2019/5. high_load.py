# Вам дана история сессий на некотором вымышленном сервисе.
# Каждая сессия характеризуется временем начала и временем окончания si и fi, для удобства все эти значения различны.
#
# Найдите такой момент времени t, когда было активно наибольшее количество сессий.
# Если таких моментов несколько, то выведите самый ранний из них. Ограничение времени: 1 с, ограничение памяти: 256 Мб.
###
# Формат ввода:
# В первой строке входных данных записано целое число n (1 ≤ n ≤ 1000).
# Далее в n строках записано через пробел по два целых числа si и fi (0 ≤ si < fi ≤ 1 000 000 000).
#
# Формат вывода:
# Выведите искомый момент времени t.
n = int(input())
session_lst = []

for _ in range(n):
    si, fi = map(int, input().split())
    session_lst.append((si, fi))

events = []
for start, end in session_lst:
    events.append((start, 1))
    events.append((end, -1))
events.sort()

max_number = min_time = cur_number = 0
for cur_time, operation in events:
    cur_number = cur_number + operation
    if cur_number > max_number:
        max_number = cur_number
        min_time = cur_time

print(min_time)

# Решение:
# Простой, но не самый эффективный алгоритм — пройтись по всем сессиям и каждую сравнить с остальными,
# посчитав количество пересечений и найдя максимальное значение. Сложность этого алгоритма — O(N x N).
#
# Но есть более оптимальный алгоритм. Для начала преобразуем список всех сессий в список событий двух типов —
# начало сессии и окончание сессии. Отсортируем эти события.
# Теперь, проходя по ним, мы будем прибавлять единицу к количеству одновременно активных сессий,
# если событие — это начало сессии и вычитать, если событие — окончание сессии.
# Сложность такого алгоритма — O(N x log N).
