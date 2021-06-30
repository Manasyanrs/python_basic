def sum_digits_in_number(number):
    results = 0
    for element in str(number):
        results += int(element)
    return results


def count_digits_in_number(number):
    total = 0
    for element in str(number):
        total += 1
    return total


questions = int(input("Введите число: "))

sum_digits = sum_digits_in_number(questions)
count_digits = count_digits_in_number(questions)
total_digits = count_digits_in_number(sum_digits) + count_digits_in_number(count_digits)
difference = sum_digits - count_digits

print("\nСумма цифр:", sum_digits)
print("Кол-во цифр в числе:", count_digits)
if total_digits == difference:
    print("Разность суммы и кол-ва цифр:", difference)

# зачет!
