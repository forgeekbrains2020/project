"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def out_personal_info(name='Имя', surname='Фамилия', was_born='Год', city='Город', email='email',
                      phone='Номер телефона'):
    """
    Возвращает данные о пользователе одной строкой
    :param name: имя
    :param surname: фамилия
    :param was_born: год рождения
    :param city: город
    :param email: адрес электронной почты
    :param phone: телефон
    :return: данные о пользоателе в виде одной строки
    """
    return print(
        f'{name} {surname} {was_born} года рождения, проживает(ал) в городе {city}, email: {email}, телефон: {phone}')


out_personal_info(name="Александр", surname="Пушкин", was_born='1799', city='Москва', email='отсутсвует',
                  phone='отсутсвует')
out_personal_info(name="Александр", was_born='1799', city='Москва', email='отсутсвует',
                  phone='отсутсвует')