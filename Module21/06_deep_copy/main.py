def total(file, product_name):
    for key, value in file.items():
        if key == "title":
            file[key] = "Куплю/продам {} недорого".format(product_name)
        elif key == "h2":
            file[key] = "У нас самая низкая цена на {}".format(product_name)
        else:
            if isinstance(value, dict):
                total(value, product_name)

    return file


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
count = int(input("Сколько сайтов: "))
for _ in range(count):
    name = input("Введите название продукта для нового сайта: ")
    print("Сайт для {}:".format(name))
    result = total(site, name)
    print(result)
