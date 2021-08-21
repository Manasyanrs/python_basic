def calculate(info):
    try:
        first = int(info[0])
        second = int(info[2])
        if info[1] == "+":
            print(first + second)
        if info[1] == "/":
            print(first / second)
        if info[1] == "%":
            print(first % second)
        if info[1] == "//":
            print(first // second)
    except ValueError:
        print("Операнды должны быть числомы.")
    except ZeroDivisionError:
        print("На 0 делить нельзя.")


try:
    with open("masige.txt", "r") as calc:
        for information in calc.readlines():
            calculate(information.split())
except FileNotFoundError:
    print("Файл не найден")
