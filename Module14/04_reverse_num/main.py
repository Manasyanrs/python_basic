
def revers_number(number):
    first = ""
    second = ""
    flags = True
    for element in str(number):
        if element == ".":
            flags = False
        elif flags:
            first = element + first
        else:
            second = element + second

    total = float(first + "." + second)
    return total


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

first_results = revers_number(first_number)
second_results = revers_number(second_number)
total_sum_numbers = first_results + second_results

print("\nПервое число наоборот:", first_results)
print("Второе число наоборот:", second_results)
print("Сумма:", total_sum_numbers)

# зачет!
