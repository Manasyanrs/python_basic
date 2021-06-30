first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))
numbers_2_years = ""
sum_2_year = str(first_year) + str(second_year)

for element in sum_2_year:
    if element not in numbers_2_years:
        numbers_2_years += element

print("Года от", first_year, "до", second_year, "с тремя одинаковыми цифрами:")

count_element = 0
for element in numbers_2_years:
    for number in range(first_year, second_year + 1):
        for number_element in str(number):
            if element == number_element:
                count_element += 1
            else:
                count_element = count_element

        if count_element == 3:
            if first_year <= number <= second_year:
                print(number)
                count_element = 0
        else:
            count_element = 0

# зачет!
