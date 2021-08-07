def find_digit(name_file, number):
    if number not in name_file:
        print("\nВ кортеже нету числа", number)
        return tuple()
    elif name_file.count(number) == 1:
        index_number = name_file.index(number)
        print("\nВ кортеже один", number)
        return name_file[index_number:]
    else:
        print("\nВ кортеже число", number, "две или бопьше")
        new_file = []
        iterations = 0
        temporary_id = 0
        for index, digit in enumerate(name_file):
            if digit == number:
                temporary_id += index
                iterations += 1
                if iterations >= 2:
                    temporary_id = temporary_id - index
                    new_file.append(name_file[temporary_id:index + 1])
                    temporary_id = index
        return tuple(new_file)


test = (25, 1, 2, 5, 3, 4, 5, 6, 15, 7, 5, 11)
search_number = int(input("Введите число для пойска в кортеже: "))

print(find_digit(test, search_number))

# зачет!
