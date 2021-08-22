import random


def division_1(number_x, number_y):
    number_x += random.randint(0, 5)
    number_y += random.randint(0, 10)
    try:
        return str(number_x / number_y)
    except ZeroDivisionError:
        print("В первой функции произошла ошибка.\nНа 0 делить нельзя.")


def division_2(number_x, number_y):
    number_x -= random.randint(0, 5)
    number_y -= random.randint(0, 10)
    try:
        return str(number_y / number_x)
    except ZeroDivisionError:
        print("Во втарой функции произошла ошибка.\nНа 0 делить нельзя.")


count_iteration = 0
try:
    with open('coordinates.txt', 'r') as read_file:
        for line in read_file.readlines():
            numbers = line.split()
            count_iteration += 1
            try:
                result_1 = division_1(int(numbers[0]), int(numbers[1]))
                result_2 = division_2(int(numbers[0]), int(numbers[1]))
                random_number = str(random.randint(0, 100))
                total_result = sorted([result_1, result_2, random_number])

                with open('result.txt', 'w') as write_file:
                    write_file.write(' '.join(total_result))
            except ValueError:
                print("Ошыбка в типе данних.\nСмотрите в фийле {file_name}, строка {line}".format(
                    file_name=read_file.name,
                    line=count_iteration
                ))

except FileNotFoundError:
    print("Файла с таким названием не сушествует.")
