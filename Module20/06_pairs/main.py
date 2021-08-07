import random

# part 1
original = list(range(10))
result = [(digit, digit + 1) for digit in original if digit % 2 == 0]
print(original)
print(result, "\n")

# part 2

original_1 = [random.randint(1, 22) for _ in range(10)]
results_1 = []
id_digit = 0
for index, digit in enumerate(original_1):
    if index % 2 == 0:
        id_digit = digit
    else:
        results_1.append((id_digit, digit))
print(original_1)
print(results_1, "\n")

# part 3

even = []
odd = []
even_odd = [(even.append(number) if number % 2 == 0 else odd.append(number)) for number in original]
result_3 = list(zip(even, odd))
print(result_3, "\n")

# part 4

even_1 = list(range(0, 10, 2))
odd_1 = list(range(1, 11, 2))
result_4 = list(zip(even_1, odd_1))
print(result_4)

# зачет!
