class MyDict(dict):
    def __getitem__(self, item):
        self.item = item

    def get(self, key, default=0):
        return super().get(key, default)


test_file = {
    "address": "123.456.840.2",
    "name": "NAME",
    "symbol": "!@#$%^&*"
}

test = MyDict(test_file)
print(test.get("address"))
print(test.get(5))
print(test.get("name"))
