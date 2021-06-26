questions = int(input("Введите число: "))


def sum_numbers(number):
    number_sum = 0
    while number != 0:
        mod = number % 10
        number_sum += mod
        number //= 10
    return number_sum


def coun_numbers(number):
    count_number = 0
    while number != 0:
        mod = number % 10
        count_number += 1
        number //= 10
    return count_number


number_sum = sum_numbers(questions)
number_count = coun_numbers(questions)
results = number_sum - number_count
total = coun_numbers(number_sum) + coun_numbers(number_count)
print("Сумма цифр:", number_sum)
print("Кол-во цифр в числе:", number_count)
if results == total:
    print("Разность суммы и кол-ва цифр:", total)
else:
    print("Разность суммы", results, "кол-ва цифр", total)