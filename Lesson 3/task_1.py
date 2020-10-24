"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def input_number():
    """
    Выполняет прием пользовательского ввода и проверяет введено ли число.
    :return: возращает число в формате  float
    """
    try:
        number = float(input('Введите число для деления: '))
    except:
        print(f"Ошибка ввода, введите число!")
    return number


def division_two_numbers(dividend, divider):
    """
    Возращает частное от деления
    :param dividend: делимое
    :param divider: делитель
    :return: частное
    """

    try:
        res = dividend / divider
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
        return
    print(f"{res:.4f}")
    return res


division_two_numbers(input_number(), input_number())
