
names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

even_names = []

for index, name in enumerate(names):
    if index % 2 == 1:
        even_names.append(name)

print("Список имен\n", names)
print("\nКаждое второе имя из списка\n", even_names)

# зачет!
