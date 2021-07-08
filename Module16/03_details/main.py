shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

questions = input("Название детали: ")
names_products = 0
total_price_products = 0

for products, price in shop:
    if products == questions:
        names_products += 1
        total_price_products += price

if names_products == 0:
    print("К сожалению у нас нет таких деталей")
else:
    print("Кол-во деталей -", names_products)
    print("Общая стоимость -", total_price_products)

# зачет!
