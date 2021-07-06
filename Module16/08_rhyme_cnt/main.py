count_peoples = int(input("Кол-во человек: "))
number = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", number, "человек")
count_peoples = list(range(1, count_peoples + 1))

while True:
    print("\nТекущий круг людей:", count_peoples)
    start_number = int(input("Начало счёта с номера "))

    if start_number not in count_peoples:
        print("Человек с номером", start_number, "нету в списке")

    else:
        results = count_peoples.index(start_number)
        formula = (results + number) % len(count_peoples) - 1
        out = count_peoples[formula]
        count_peoples.remove(count_peoples[formula])
        print("Выбывает человек под номером", out)

    if len(count_peoples) == 1:
        print()
        print("Остался человек под номером", count_peoples[0])
        break

# зачет!
