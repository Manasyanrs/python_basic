count_number = int(input("Кол-во чисел: "))
total_numbers = []

for _ in range(count_number):
    number = int(input("Число: "))
    total_numbers.append(number)

new_numbers = total_numbers[::-1]

print("\nПоследовательность:", end=" ")

for element in total_numbers:
    print(element, end=" ")

for _ in total_numbers:
    if total_numbers[-1] == new_numbers[0]:
        new_numbers.remove(new_numbers[0])

    else:
        total_numbers.extend(new_numbers)
        break

length = len(new_numbers)

print("\nНужно приписать чисел:", length)
print("Сами числа:", end=" ")
for element in new_numbers:
    print(element, end=" ")
