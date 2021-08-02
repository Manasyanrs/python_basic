count_order = int(input("Введите количество заказов: "))
menu_pizzas = []
clients_database = dict()
print("Покупатель | название пиццы | количество заказанных пицц.")

for number in range(1, count_order + 1):
    order = input("{} заказ: ".format(number)).split()
    surname_client = order[0]
    pizza_name = order[1]
    count_pizza = order[2]
    update = {pizza_name: count_pizza}

    if surname_client not in clients_database:
        clients_database[surname_client] = {pizza_name: order[2]}
        menu_pizzas.append(pizza_name)
    else:
        if pizza_name in menu_pizzas:
            for count in clients_database[surname_client][pizza_name]:
                clients_database[surname_client][pizza_name] = str(int(count) + int(order[2]))
                break
        else:
            clients_database[surname_client].update(update)
            menu_pizzas.append(pizza_name)

for surname in clients_database:
    print(surname + ":")
    for pizzas in clients_database[surname]:
        print("     " + pizzas + ": " + clients_database[surname][pizzas])
