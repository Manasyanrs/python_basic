
# TODO применить рекомендации данные ранее
# TODO типы в именовании функций и переменных не указываем
def float_in_tuple(tuple_file):
    new_tuple = sorted(tuple_file)
    count_float = 0
    for digit in new_tuple:
        if type(digit) == float:
            count_float += 1
            break

    if count_float == 0:
        print("В кортеже нету числа с точкой")
        return new_tuple
    else:
        print("В кортеже есть число с точкой")
        return tuple_file


total_numbers = (1, 8, 5, 4, 9, 25, 6.5)

result = float_in_tuple(total_numbers)
print(result)
