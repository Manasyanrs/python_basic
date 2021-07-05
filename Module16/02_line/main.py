students_a = list(range(160, 176, 2))
students_b = list(range(160, 182, 3))

print("Ученики класса 'а' по росту\n", students_a)
print("\nУченики класса 'б' по росту\n", students_b)
students_a.extend(students_b)
students_a.sort()
print("\nПосле объединенные 2 класса\n", students_a)
