
names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

even_names = []

for name_id in range(len(names)):

    if name_id % 2 == 1:
        even_names.append(names[name_id])

print("Список имен\n", names)
print("\nКаждое второе имя из списка\n", even_names)