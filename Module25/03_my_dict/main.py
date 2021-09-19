class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


test_file = {
    "address": "123.456.840.2",
    "name": "NAME",
    "symbol": "!@#$%^&*"
}

test = MyDict()
print(test.get(5))
# TODO при такой кострукции не работет метод если ключ есть
print(test.get("name"))     # Ответ 0
