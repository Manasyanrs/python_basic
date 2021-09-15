# TODO наледоваться от dict
class MyDict:
    def __init__(self, file):
        self.file = file

    def get(self, key, info=""):
        # TODO сильно усложнили нужно просто переопределитть родительский класс
        for name in self.file:
            if key == name:
                return key
            else:
                if len(info) > 0:
                    return info
                else:
                    return 0

# TODO запустить
