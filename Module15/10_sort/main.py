initial = [1, 4, -3, 0, 10]
print("Изначальный список:", initial)

for index in range(len(initial)):
    for element in range(index + 1, len(initial)):
        if initial[index] > initial[element]:
            initial[index], initial[element] = initial[element], initial[index]

print("Отсортированный список:", initial)
# part 2
print()
initial.sort()
print("Отсортированный список:", initial)
