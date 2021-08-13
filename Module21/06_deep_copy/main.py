def total(file, product_name, count_size):
    for _ in range(count_size):
        for k, v in file.items():
            if k == "title":
                file[k] = "Куплю/продам {} недорого".format(product_name)
            elif k == "h2":
                file[k] = "У нас самая низкая цена на {}".format(product_name)
            else:
                if isinstance(v, dict):
                    total(v, product_name, count_size)

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
name = input("Введите название продукта для нового сайта: ")
print("Сайт для {}:".format(name))
result = total(site, name, count)
print(result)
