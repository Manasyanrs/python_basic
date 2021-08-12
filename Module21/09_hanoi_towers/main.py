def move(n, x, y):
    if n % 2 == 0:
        if n > 0:
            move(n - 1, x, y-1)
            print("Переложить диск {disc} со стержня номер {rod_2} на стержень номер {rod_3}".format(
                disc=n,
                rod_2=x,
                rod_3=y
            ))
            move(n - 1, y - 1, y)
    else:
        if n > 0:
            move(n - 1, x, y + 1)
            print("Переложить диск {disc} со стержня номер {rod_2} на стержень номер {rod_3}".format(
                disc=n,
                rod_2=x,
                rod_3=y
            ))
            move(n - 1, y - 1, y)


number = int(input("Введите количество дисков: "))
if number % 2 == 0:
    move(number, 1, 3)
else:
    move(number, 1, 2)
