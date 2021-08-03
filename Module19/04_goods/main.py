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

for name, product_code in goods.items():
    if product_code in store:
        total_quantity = 0
        total_price = 0
        for count in store[product_code]:
            total_quantity += count["quantity"]
            total_price += count["quantity"] * count["price"]
        print("{name_product} - {quantity} шт, стоимость {price_product} руб".format(
            name_product=name,
            quantity=total_quantity,
            price_product=total_price
        ))
    else:
        print("{} продукт с таким кодом не найден".format(product_code))
