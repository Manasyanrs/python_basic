def find_dotted_number(file):
    new_file = sorted(file)
    count_dotted_number = 0
    for digit in new_file:
        if type(digit) == float:
            count_dotted_number += 1
            break

    if count_dotted_number == 0:
        print("В кортеже нету числа с точкой")
        return new_file
    else:
        print("В кортеже есть число с точкой")
        return file


total_numbers = (1, 8, 5, 4, 9, 25, 6.5)

result = find_dotted_number(total_numbers)
print(result)
