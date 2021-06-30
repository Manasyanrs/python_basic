
my_element = [1, 4, -3, 0, 10]

shift = int(input("Сдвиг: "))

print("\nИзначальный список:", my_element)
new_element = []
for _ in range(len(my_element)):
    if shift == 1:
        new_element = my_element[shift:] + my_element[:shift]
    else:
        new_element = my_element[shift - 1:] + my_element[:shift - 1]
print("Сдвинутый список:", new_element)