from collections.abc import Iterable


class QHofstadter:
    def __init__(self, file: list) -> None:
        self.__file = file
        self.__counter = 0

    def get_file(self):
        return self.__file

    def __next__(self) -> int:
        if self.__counter < len(self.__file):
            result = self.__file[-self.__file[-1]] + self.__file[-self.__file[-2]]
            self.__file.append(result)
            self.__counter += 1
            return result

        else:
            raise StopIteration

    def __iter__(self) -> Iterable:
        return self


hofstadter = QHofstadter([1, 1])
for _ in range(10):
    if hofstadter.get_file() == [1, 2]:
        print("Нельзя передать значения", end=" ")
        break
    next(hofstadter)

print(hofstadter.get_file())
