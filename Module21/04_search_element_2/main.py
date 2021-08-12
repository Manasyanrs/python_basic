def search_key(file, key, search_depth):
    if search_depth != 0:
        if key in file:
            return file[key]
        else:
            for element in file.values():
                if type(element) == dict:
                    result = search_key(element, key, search_depth - 1)
                    if result is not None:
                        return result


site = {
        'html': {
            'head': {
                    'title': 'Мой сайт'
                    },
            'body': {
                    'h2': 'Здесь будет мой заголовок',
                    'div': 'Тут, наверное, какой-то блок',
                    'p': 'А вот здесь новый абзац'
                    }
                }
}


find_key = input("Введите ключ для поиска значения: ")
depth = int(input("Введите глубину поиска: "))

find = search_key(site, find_key, depth)
if find:
    print(find)
else:
    print("В глубине {} нету токого ключа".format(depth))
