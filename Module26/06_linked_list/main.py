from collections.abc import Iterable


class LinkedList:
    def __init__(self) -> None:
        self.__result = []
        self.__counter = 0

    def append(self, element: int) -> None:
        self.__result.append(element)

    def get(self, element: int) -> int:
        for index, value in enumerate(self.__result):
            if index == element:
                return value

    def remove(self, element: int) -> None:
        for index, value in enumerate(self.__result):
            if index == element:
                self.__result.pop(self.__result.index(value))

    def __str__(self) -> str:
        return "{}".format(self.__result)

    def __iter__(self) -> Iterable:
        self.index = 0
        return self

    def __next__(self) -> int:
        if self.__counter < len(self.__result):
            self.__counter += 1
            number = self.__result[self.index]
            self.index += 1
            return number
        else:
            raise StopIteration


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(50)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

for digit in my_list:
    print(digit)
