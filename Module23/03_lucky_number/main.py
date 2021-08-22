total_result = 0
count = 0
while True:
    if total_result >= 777:
        print("Сумма чисел больше либо равна 777.")
        break
    try:
        if count == 13:
            raise Warning("Программа приостановлено случанием исключением")
        question = int(input("Введите число: "))
        total_result += question
        with open("numbers.txt", "a") as digit:
            digit.write("{}\n".format(str(question)))
    except ValueError:
        print("Введите целое число.")
    except Warning:
        raise Warning("Программа выбрасывала с вероятностью 1 к 13")

# зачет!
