def move(number, rod_x, rod_y):
    if number % 2 == 0:
        if number > 0:
            move(number - 1, rod_x, rod_y-1)
            print("Переложить диск {disc} со стержня номер {rod_2} на стержень номер {rod_3}".format(
                disc=number,
                rod_2=rod_x,
                rod_3=rod_y
            ))
            move(number - 1, rod_y - 1, rod_y)
    else:
        if number > 0:
            move(number - 1, rod_x, rod_y + 1)
            print("Переложить диск {disc} со стержня номер {rod_2} на стержень номер {rod_3}".format(
                disc=number,
                rod_2=rod_x,
                rod_3=rod_y
            ))
            move(number - 1, rod_y - 1, rod_y)


count_disks = int(input("Введите количество дисков: "))
if count_disks % 2 == 0:
    move(count_disks, 1, 3)
else:
    move(count_disks, 1, 2)

# зачет!
