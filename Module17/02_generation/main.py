number = int(input("Введите длину списка: "))

results = [(digit * 0 + 1 if digit % 2 == 0 else digit % 5) for digit in range(number)]
print("Результат:", results)
