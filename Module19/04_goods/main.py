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
    product_count = 0
    product_cost = 0
    for element in store[product_code]:
        product_count += element["quantity"]
        product_cost += element["price"] * element["quantity"]
    print("{name_product} - {quantity} шт, стоимость {price_product} руб".format(
        name_product=name,
        quantity=product_count,
        price_product=product_cost
    ))

# зачет!
