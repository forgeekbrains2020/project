"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
# Решение без генераторного выражения
final_list = []
original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
previos = original_list[0] + 1

for item in original_list:
    if item > previos:
        final_list.append(item)
    previos = item
print(f"{final_list}")

# Решение с генераторным выражением
new_list = [el for indx, el in enumerate(original_list) if indx > 0 and (original_list[indx] > original_list[indx - 1])]
print(f"{new_list}")
