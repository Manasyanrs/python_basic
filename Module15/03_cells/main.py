questions = int(input("Кол-во клеток: "))
improper_cell = []
print()
for numbers in range(1, questions + 1):
    new_questions = int(input("Эффективность " + str(numbers) + " клетки: "))
    if numbers > new_questions:
        improper_cell.append(new_questions)

print("\nНеподходящие значения:", end=" ")
for improper in improper_cell:
    print(improper, end=" ")

# зачет!
