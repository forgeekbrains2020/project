"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [71, 15, 13, 13, 12, 2]
raiting = int(input("Введите элемент рейтинга: "))
out = False
if raiting in my_list:
    #print(f"Число {raiting} в рейтинге")
    my_list.insert((my_list.index(raiting) + my_list.count(raiting)), raiting)
else:
    for ind, el in enumerate(my_list):
        if raiting > el:
            my_list.insert(ind, raiting)
            out = True
            break
    if out != True:
        my_list.insert(len(my_list) + 1, raiting)
#print(f"Пользователь ввел чилсло {raiting}. Результат: {','.join(my_list)}.")
print(type(my_list))
#test = ','.join((my_list))
print(f"Пользователь ввел чилсло {raiting}. Результат: {my_list}")
#print                                        (f"{ind}. {''.join(list(item)[:10])}")