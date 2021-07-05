count_rollers = int(input("Кол-во коньков: "))
rollers = []

for number in range(1, count_rollers + 1):
    size = int(input("Размер " + str(number) + " пары: "))
    rollers.append(size)

print()
peoples = int(input("Кол-во людей: "))
count_people = 0

for count in range(1, peoples + 1):
    size_foot = int(input("Размер ноги " + str(count) + " человека: "))
    if size_foot in rollers:
        rollers.remove(size_foot)
        count_people += 1

print("\nНаибольшее кол-во людей, которые могут взять ролики:", count_people)

# зачет!
