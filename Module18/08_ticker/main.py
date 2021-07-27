first_line = input("Первая строка: ")
second_line = input("Вторая строка: ")
count = 0
results = ""
if first_line == second_line:
    print("Первая строка идентичен к второму строку")

else:
    for i in range(1, len(second_line) + 1):
        count += 1
        results = results + second_line[-i:] + second_line[:-i]
        if results == first_line:
            print("Первая строка получается из второй со сдвигом", count)
            break

        else:
            results = ""

if len(second_line) == count:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")