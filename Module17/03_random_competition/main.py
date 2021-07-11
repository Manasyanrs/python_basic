import random

first_command = [random.uniform(5, 10) for _ in range(20)]
first = [round(numbers, 2) for numbers in first_command]

second_command = [random.uniform(5, 10) for _ in range(20)]
second = [round(numbers, 2) for numbers in second_command]

results = [(first[digit] if first[digit] > second[digit] else second[digit]) for digit in range(20)]

print("Первая команда:", first)
print("Вторая команда:", second)
print("Победители тура:", results)
