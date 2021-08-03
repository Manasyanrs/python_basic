goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# TODO используем .items() у словаря и получаем сразу в заголовке цикла имя и код товара
#  должно быть всего два цикла
# TODO слова list в именовании переменной быть не должно
for name in goods:
    if goods[name] in store:
        quantity = 0
        price_quantity = 0
        price = 0
        for store_list in store[goods[name]]:
            for element in store_list:
                quantity += int(store_list['quantity'])
                price_quantity += int(store_list['price'])
                price += int(int(store_list['quantity']) * int(store_list['price']))

        total_quantity = int(quantity/2)
        total_price = int(price/2)

        print(name + " -", total_quantity, "шт, стоимость", total_price, "руб")
