from collections.abc import Iterable


def generator(file_1: list, file_2: list) -> Iterable:
    new_file = zip(file_1, file_2)
    for digits in new_file:
        result = digits[0] * digits[1]
        print("{} * {} = {}".format(digits[0], digits[1], result))
        yield result


variable_1 = [2, 5, 7, 10]
variable_2 = [3, 8, 4, 9]
to_find = 56
iteration = 0

result = generator(file_1=variable_1, file_2=variable_2)
for information in result:
    if information == to_find:
        print("Нашлось!!!")
        break
    iteration = 1

if iteration == 1:
    print("Не нашлось")
