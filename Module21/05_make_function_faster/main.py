
# TODO не пишем что это функция и так понятно
def calculating_math_func(data):
    result = 1
    if data in factorials.keys():
        result = factorials[data]
    else:
        for index in range(1, data + 1):
            result *= index
        factorials[data] = result

    result /= data ** 3
    result = result ** 10
    return result


factorials = dict()

test_1 = calculating_math_func(5)
print(test_1)
test_2 = calculating_math_func(10)
print(test_2)
test_3 = calculating_math_func(5)
print(test_3)
