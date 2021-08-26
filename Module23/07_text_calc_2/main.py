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
                reformat = input("Введите исправленную строку с пробеламы: ").split()
                result += calculate(reformat)

    except ValueError:
        print("Операнды должны быть числомы")
    except ZeroDivisionError:
        print("На 0 делить нельзя.")
    return result


try:
    with open("calc.txt", "r", encoding="utf-8") as calculate_line:
        file = calculate_line.readlines()
        print("Содержимое файла {}\n".format(calculate_line.name))
        for element in file:
            print(element, end="")

        total_result = 0
        for information in file:
            total_result += calculate(information.split())
        print("\nСумма результатов:", total_result)

except FileNotFoundError:
    print("Файл с таким названием не существует.")
