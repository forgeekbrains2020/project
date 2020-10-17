"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
products_list = []
input_repeat = 'yes'
while input_repeat == 'yes' or input_repeat == 'y':
    product_num = int(input("Введите номер товара: "))
    product_name = input("Введите название товара: ")
    product_cost = float(input("Введите цену товара: "))
    product_quantity = int(input("Введите количество товара: "))
    product_unit = input("Введите единицу измерения товара: ")
    input_repeat = input("Хотите добавить еще товар? Введите (y)es или (n)o: ")
    products_list.append((product_num, {'название': product_name, 'цена': product_cost, 'количество': product_quantity,
                                        'ед': product_unit}))

analytics_dict = {}
product_names_list = []
product_costs_list = []
product_quantity_list = []
product_units_list = []

for item in products_list:
    product_names_list.append(item[1]['название'])
    product_costs_list.append(item[1]['цена'])
    product_quantity_list.append(item[1]['количество'])
    product_units_list.append(item[1]['ед'])
analytics_dict = {'названия': product_names_list, 'цены': product_costs_list, 'количества': product_quantity_list,
                  'ед': product_units_list}

print(analytics_dict)
