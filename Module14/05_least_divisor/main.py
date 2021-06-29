def minimum_divisor(number):
    results = 0
    for element in range(2, number + 1):
        if number % element == 0:
            results = element
            if results >= 2:
                break
    return results


questions = int(input("Введите число: "))
total = minimum_divisor(questions)

print("Наименьший делитель, отличный от единицы:", total)

