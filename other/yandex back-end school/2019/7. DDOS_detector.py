# Дан список из N IP-адресов.
# Назовем IP-адрес «плохим», если существует M подряд идущих строк, в которых этот IP-адрес встречается хотя бы K раз.
# Ограничение времени: 10 с, ограничение памяти: 10 МБ.
###
# Формат ввода:
# Первая строка содержит число N (1 ≤ N ≤ 10^6).
# Вторая строка содержит число M (1 ≤ M ≤ 10^3).
# Третья строка содержит число K (1 ≤ K ≤ M).
# В следующих N строках записаны IP-адреса, по одному на строку.
#
# Формат вывода:
# Выведите список «плохих» IP-адресов в лексикографическом порядке.
from collections import Counter, deque
import sys


def main():
    # Считываем числа N, M и K
    n_of_lines = int(sys.stdin.readline().strip())
    window_size = int(sys.stdin.readline().strip())
    threshold = int(sys.stdin.readline().strip())

    # Заводим множество для «плохих» адресов,
    # дек для окна последних адресов
    # и счетчик адресов
    bad_ips = set()
    last_ips = deque(maxlen=window_size)
    counter = Counter()

    for _ in range(n_of_lines):
        # Считываем IP-адрес
        current_ip = sys.stdin.readline().rstrip()

        # Проверяем, что дек заполнился
        if len(last_ips) == window_size:
            # Удаляем из дека самый старый адрес
            # и уменьшаем его счетчик на единицу
            oldest_ip = last_ips.pop()
            counter[oldest_ip] -= 1

            # Если счетчик стал равен нулю — удаляем адрес
            if not counter[oldest_ip]:
                del counter[oldest_ip]

        # Добавляем новый адрес в дек
        last_ips.appendleft(current_ip)

        # Если новый адрес уже есть в списке «плохих»,
        # то можно перейти к следующему адресу
        if current_ip in bad_ips:
            continue

        # Увеличиваем счетчик для нового адреса
        counter[current_ip] += 1

        # Если счетчик достиг порогового значения K,
        # то добавляем адрес в список «плохих»
        if counter[current_ip] >= threshold:
            bad_ips.add(current_ip)
            # Удаляем «плохой» адрес из счетчика,
            # чтобы не использовать лишнюю память
            del counter[current_ip]

    # Сортируем «плохие» адреса и выводим результат
    print('\n'.join(current_ip for current_ip in sorted(bad_ips)))


if __name__ == "__main__":
    main()

# Решение:
# Наивное решение: сохранить все адреса в список, а потом пройтись по нему окном длиной M и найти адреса,
# которых в этом окне больше K штук. Такое решение сработает на первых простых тестах,
# но дальше не пройдет из-за лимитов по памяти и по времени.
#
# Улучшение: на самом деле нам не нужен список всех адресов — достаточно иметь список M последних адресов.
# Его удобно хранить с помощью дека длины M. В деке можно искать адреса, количество которых ≥ K.
# Это более удачное решение, но поскольку на каждом шаге мы будем подсчитывать адреса в деке,
# то все равно не уложимся в лимит по времени.
#
# Чтобы на каждом шаге не пересчитывать адреса заново, будем для каждого адреса хранить счетчик —
# сколько раз он встречается в списке последних М адресов. При чтении нового адреса будем:
# — уменьшать счетчик на единицу для самого старого адреса и увеличивать на единицу для нового,
# — а затем добавлять в список «плохих» адресов новый адрес, если счетчик для него достиг K.
#
# Но это решение не уложится в лимит по памяти, если все IP-адреса уникальные.
# Тогда количество счетчиков достигнет 10^6. Однако для большинства адресов счетчик будет содержать ноль.
# Другими словами, если счетчик адреса при уменьшении достиг нуля, то достаточно удалить этот счетчик из памяти.
# Тогда количество счетчиков не превысит 10^3.
#
# Финальное решение требует O(N) времени для прохода по всем IP-адресам
# и O(M) памяти для хранения списка последних адресов и счетчиков адресов.