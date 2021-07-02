
def odd_numbers(number):
    odd_number = []

    for numbers in range(1, number + 1):
        if numbers % 2 == 1:
            odd_number.append(numbers)
    return odd_number


questions = int(input('Введите число: '))

print("Список из нечетных чисел")
odd_numbers = odd_numbers(questions)
print(odd_numbers)

# зачет!
