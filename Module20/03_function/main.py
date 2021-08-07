
# TODO не в функции не в параметре не указываем tuple
# TODO функцию функцией не называем дать ей более говорящее имя
def tuple_function(tuple_variable, number):
    if number not in tuple_variable:
        print("\nВ кортеже нету числа", number)
        return tuple()
    elif tuple_variable.count(number) == 1:
        index_number = tuple_variable.index(number)
        print("\nВ кортеже один", number)
        return tuple_variable[index_number:]
    else:
        print("\nВ кортеже число", number, "две или бопьше")
        new_tuple = []
        iterations = 0
        temporary_id = 0
        for index, digit in enumerate(tuple_variable):
            if digit == number:
                temporary_id += index
                iterations += 1
                if iterations >= 2:
                    temporary_id = temporary_id - index
                    new_tuple.append(tuple_variable[temporary_id:index + 1])
                    temporary_id = index
        return tuple(new_tuple)


test = (25, 1, 2, 5, 3, 4, 5, 6, 15, 7, 5, 11)
find_digit = int(input("Введите число для пойска в кортеже: "))

print(tuple_function(test, find_digit))
