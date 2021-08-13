def minimum_arguments(args):
    digit = sorted([len(i) for i in args])
    return digit[0]


def analog_zip(*args):
    digit = minimum_arguments(args)
    result = ()

    for index in range(digit):
        iteration_variable = ()

        for id_elements in args:
            iteration_variable += (list(id_elements)[index]),

        result += iteration_variable,

    return (element for element in result)


test_letters = ["a", "b", "c"]
test_digit = {1, 2}
test_dict = {"v": 2, 9: 4}

total_result = analog_zip(test_letters, test_digit, test_dict)
print(total_result)
for total_element in total_result:
    print(total_element)
