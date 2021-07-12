import random

number_sticks = int(input("Кол-во палок: "))
number_throws = int(input("Кол-во бросков: "))
sticks_list = list(range(1, number_sticks + 1))

for i in range(1, number_throws + 1):
    print("Бросок " + str(i) + ".", end=" ")
    left = random.randint(2, number_sticks)
    right = random.randint(left, number_sticks)
    print("Сбиты палки с номера", left, "\nпо номер", right)
    for digit in range(left, right + 1):
        for number in range(len(sticks_list)):
            if digit - 1 == number:
                sticks_list.insert(number, ".")
                sticks_list.remove(sticks_list[digit])
                break

results = ""
for element in range(len(sticks_list)):
    if sticks_list[element] != ".":
        results += "I"
    else:
        results += "."

print("\nРезультат:", results)

# TODO нейминг переменных

