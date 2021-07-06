first = []
second = []

print("Вводите 3 числа первого списка:")
for _ in range(3):
    digit = int(input("Введите число: "))
    first.append(digit)

print("\nВводите 7 числа второго списка:")

for _ in range(7):
    digit = int(input("Введите число: "))
    second.append(digit)

print("Первый список:", first)
print("Второй список:", second)

first.extend(second)

for element in first:
    for _ in first:
        number = first.count(element)
        while number > 1:
            first.remove(element)
            break

print("Новый первый список с уникальными элементами:", first)