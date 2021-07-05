shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

questions = input("Название детали: ")
names_products = 0
price_products = 0

# TODO сразу в заголовке цикла распаковываем и получаем имя и цену товара из списка который придет когда мы будем
#  итерироваться по главному списку.

for products in shop:
    if products[0] == questions:
        names_products += 1
        price_products += products[1]

print("Кол-во деталей -", names_products)
print("Общая стоимость -", price_products)
