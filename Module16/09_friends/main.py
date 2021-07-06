count_friends = int(input("Кол-во друзей: "))
count_friends = [0] * count_friends
debt = int(input("Долговых расписок: "))

print()
for number in range(1, debt + 1):
    print(number, "расписка")
    whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    price = int(input("Сколько: "))

    if whom:
        count_friends[whom - 1] -= price
        count_friends[from_whom - 1] += price
    print()

print("\nБаланс друзей:")
for money in range(len(count_friends)):
    number_friends = money + 1
    print(number_friends, ":", count_friends[money])

# зачет!
