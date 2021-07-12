register = [4, 0, 7, 12, 0, 46, 9, 0, 3]
print("Список из целых чисел", register)

for digit in range(len(register)):
    if register[digit] == 0:
        register.append(register[digit])
        register.remove(register[digit])

print("Список после сжатие", register)

count_zero = 0

for number in range(len(register)):
    if register[number] == 0:
        count_zero += 1

register = register[:-count_zero]
print("Список без нулей", register)
