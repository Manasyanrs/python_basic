
# TODO вот такая реализация в инит ничего не добавляем потому что можем сломать логику
# class MyDict(dict):
#     def get(self, key, default=0):
#         return super().get(key, default)


class MyDict(dict):
    def __init__(self, file):
        self.file = file
        super().__init__()

    def get(self, key):
        if key in self.file:
            return self.file[key]

        else:
            return 0


test_file = {
    "address": "123.456.840.2",
    "name": "NAME",
    "symbol": "!@#$%^&*"
}

test = MyDict(test_file)
print(test.get(5))
print(test.get("name"))
