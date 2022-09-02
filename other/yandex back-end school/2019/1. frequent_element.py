# Дан массив a из n целых чисел. Напишите программу, которая найдёт число, которое чаще других встречается в массиве.
# Ограничение времени: 2 с, ограничение памяти: 256 Мб.
###
# Формат ввода:
# В первой строке входных данных записано число n (1 ≤ n ≤ 300_000).
# Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1_000_000_000).
#
# Формат вывода:
# Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
frequency_counter = Counter(a)

result = a[0]
max_count = frequency_counter[result]
for number, count in frequency_counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print(result)

# O(n) времени на проход по массиву и потом по словарю.
# O(n) дополнительной памяти на словарь.
# Решение:
# Простая задача, которую можно решить как с использованием обычного словаря,
# так и с использованием структуры Counter из модуля collections.
#
# Сначала можно посчитать, сколько раз встречается каждый элемент, затем выбрать наибольший из тех,
# которые встречаются наибольшее число раз. Решение требует O(n) времени и O(n) дополнительной памяти.
# from collections import Counter
#
# n = int(input())
# a = [int(i) for i in input().split()]
#
# counter = Counter(a)
#
# result = a[0]
# max_count = counter[result]
# for number, count in counter.items():
#     if count > max_count or (count == max_count and number > result):
#         result = number
#         max_count = count
#
# print(result)
