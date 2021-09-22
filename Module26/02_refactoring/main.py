from collections.abc import Iterable


def generator(file_1: list, file_2: list) -> Iterable:
    for digit in file_1:
        for number in file_2:
            # TODO переменные не должны пересекаться
            result = digit * number
            print("{} * {} = {}".format(digit, number, result))
            yield result


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

result = generator(file_1=list_1, file_2=list_2)
for information in result:
    if information == to_find:
        print("Found!!!")
        break

# TODO нейминг
