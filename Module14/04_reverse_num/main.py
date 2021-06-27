first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
def revers_number(number):
    first_number = ""
    second_number = ""
    flags = True
    for element in str(number):
        if element == ".":
            flags = False
        elif flags:
            first_number = element + first_number
        else:
            second_number = element + second_number

    total = float(first_number + "." + second_number)

    return total

first_results = revers_number(first_number)
second_results = revers_number(second_number)
total_sum_numbers = first_results + second_results

print("Первое число наоборот:", first_results)
print("Второе число наоборот:", second_results)
print("Сумма:", total_sum_numbers)


