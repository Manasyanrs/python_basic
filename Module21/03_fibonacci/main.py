# part 1
def fibonacci_digits(number_id):
    first_digit = 0
    second_digit = 1
    for _ in range(number_id):
        first_digit, second_digit = second_digit, first_digit + second_digit
    return first_digit


# part 2
def fibonacci_digits_1(number_id):
    if number_id == 1 or number_id == 2:
        return 1
    elif number_id == 0:
        return 0
    else:
        return fibonacci_digits_1(number_id - 1) + fibonacci_digits_1(number_id - 2)


# part 1
question = int(input("Введите позицию числа в ряде Фибоначчи: "))
result = fibonacci_digits(question)
print("\nЧисло:", result)

# part 2
print()
result = fibonacci_digits_1(question)
print("Число:", result)
