"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def sum_two_max_numbers(num1, num2, num3):
    """
    Возвращает сумму наибольших двух аргументов из трех с помощь функции sort
    :param num1: первое число
    :param num2: второе число
    :param num3: третье число
    :return: сумма наибольших двух аргументов
    """
    my_list = [num1, num2, num3]
    my_list.sort()
    return my_list[1] + my_list[2]


print(sum_two_max_numbers(32, 5, 3))


def sum_2_max_numbers(num1, num2, num3):
    """
        Возвращает сумму наибольших двух аргументов из трех без помощи функции sort
        :param num1: первое число
        :param num2: второе число
        :param num3: третье число
        :return: сумма наибольших двух аргументов
        """
    if num1 >= num2:
        max = num1
        min = num2
    else:
        max = num2
        min = num1
    sum += max
    if min >= num3:
        sum += min
    else:
        sum += num3
    return sum


print(sum_two_max_numbers(4, 5, 3))
print(sum_two_max_numbers(3, 5, -4))
