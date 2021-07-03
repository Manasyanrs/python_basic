first_number = [1, 5, 3]
second_number = [1, 5, 1, 5]
third_number = [1, 3, 1, 5, 3, 3]

first_number.extend(second_number)
count_numbers = first_number.count(5)
print("Кол-во цифр 5 при первом объединении:", count_numbers)

first_number.extend(third_number)
count_numbers = first_number.count(3)
print("Кол-во цифр 3 при втором объединении:", count_numbers)

print("Итоговый список:", first_number)
