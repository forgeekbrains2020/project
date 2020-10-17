"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

my_list = [12, -1.5, "строка", ["список", 2], True, None, ('my_typle', 2), {3,4}, frozenset('abrakadabra'), {"my_dic": 5}, b'text', bytearray(b"some text")]

for el in my_list:
    print(type(el))