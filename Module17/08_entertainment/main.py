import random

count_sticks = int(input("Количество палок: "))
count_throws = int(input("Количество бросков: "))
stick_number = list(range(1, count_sticks + 1))

for throws in range(1, count_throws + 1):
    print("Бросок " + str(throws) + ".", end=" ")
    left = random.randint(2, count_sticks)
    right = random.randint(left, count_sticks)
    print("Сбиты палки с номера", left, "\nпо номер", right)
    for digit in range(left, right + 1):
        for number in range(len(stick_number)):
            if digit - 1 == number:
                stick_number.insert(number, ".")
                stick_number.remove(stick_number[digit])
                break

results = ""
for element in range(len(stick_number)):
    if stick_number[element] != ".":
        results += "I"
    else:
        results += "."

print("\nРезультат:", results)
