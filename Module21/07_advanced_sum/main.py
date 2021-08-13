def advanced_sum(*args):
    result = 0
    for element in args:
        if isinstance(element, int):
            result += element
        else:
            for digit in element:
                if isinstance(digit, int):
                    result += digit
                else:
                    result += advanced_sum(digit)
    return result


test_1 = advanced_sum([[1, 2, [3]], [1], 3, [3, 4]])
print(test_1)
print()
test_2 = advanced_sum(1, 2, 3, 4, 5, (1, 4))
print(test_2)

# зачет!
