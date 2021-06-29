first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

# TODO Параметры как и имя функции не должны подчеркиваться и пересекаться с глобальными переменными
# TODO функции объявляем всегда выше
def revers_number(number):
    first_number = ""
    second_number = ""
    flags = True
    for element in str(number):
        if element == ".":
            flags = False
        elif flags:
            first_number = element + first_number
        else:
            second_number = element + second_number

    total = float(first_number + "." + second_number)

    return total

first_results = revers_number(first_number)
second_results = revers_number(second_number)
total_sum_numbers = first_results + second_results

print("Первое число наоборот:", first_results)
print("Второе число наоборот:", second_results)
print("Сумма:", total_sum_numbers)

# Начиная с этого модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Можно привести все к нужному формату code\Reformat code

# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме

