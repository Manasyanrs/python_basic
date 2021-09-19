class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


# TODO а как наш класс знает о этом объекте ?
test_file = {
    "address": "123.456.840.2",
    "name": "NAME",
    "symbol": "!@#$%^&*"
}

test = MyDict()
# TODO чтобы в нем были данные в него нужно что то добавить сейчас он пуст
print(test.get(5))
# при такой кострукции не работет метод если ключ есть
print(test.get("name"))     # Ответ 0
