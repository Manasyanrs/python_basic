def calculate(info):
    result = 0
    try:
        first = int(info[0])
        second = int(info[2])
        if info[1] == "*":
            result += (first * second)
        if info[1] == "+":
            result += (first + second)
        if info[1] == "/":
            result += (first / second)
        if info[1] == "%":
            result += (first % second)
        if info[1] == "//":
            result += (first // second)
        if len(info[1]) > 1:
            print("\nСодержимое консоли:")
            question = input("Обнаружена ошибка в строке: {} {} {}  Хотите исправить? ".format(
                first, info[1], second)).lower()
            if question == "да":
                reformat = input("Введите исправленную строку: ").split()
                result += calculate(reformat)

    except ValueError:
        print("Операнды должны быть числомы")
    except ZeroDivisionError:
        print("На 0 делить нельзя.")
    return result


with open("message.txt") as calculate_line:
    print("Содержимое файла {}\n{}".format(calculate_line.name, calculate_line.read()))

total_result = 0
with open("message.txt") as calculate_line:
    for information in calculate_line.readlines():
        total_result += calculate(information.split())

print("\nСумма результатов:", total_result)
