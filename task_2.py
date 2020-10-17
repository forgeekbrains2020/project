"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
my_digits = input('Введите целые числа через пробел: ')
my_list = my_digits.split()
len_my_list = len(my_list)

if len_my_list % 2 == 0:
    last_pos = len_my_list - 1
else:
    last_pos = len_my_list - 2
now_pos = 0

while now_pos < last_pos:
    my_tmp = my_list[now_pos]
    my_list[now_pos] = my_list[now_pos + 1]
    my_list[now_pos + 1] = my_tmp
    now_pos += 2

for el in my_list:
    print(el, end=' ')
