# TODO принимаем арги
def analog_zip(variable_1, variable_2):
    # TODO в общем используем связку range + len + sorted
    length = min(len(variable_1), len(variable_2))
    return ((list(variable_1)[index], list(variable_2)[index])
            for index, _ in enumerate(range(length)))

# TODO вторая функция как раз примет variable_1, variable_2
# TODO и вернет генератор который вы запустите по первой функции

test_letters = ["a", "b", "c"]
test_digit = {1, 2}

result = analog_zip(test_letters, test_digit)
print(result)
for element in result:
    print(element)
