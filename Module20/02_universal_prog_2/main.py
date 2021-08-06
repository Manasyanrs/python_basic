def is_prime(number):
    prime_numbers = []
    for digit in number:
        if digit != 0 and digit != 1:
            flag = True
            for element in range(2, digit):
                if digit % element == 0:
                    flag = False
            if flag:
                prime_numbers.append(digit)
    return prime_numbers


def prime_indices(all_type):
    all_index = []
    for index, _ in enumerate(all_type):
        all_index.append(index)

    return is_prime(all_index)


test_1 = "Hlello Python"
test_2 = list(range(25))
test_3 = {number: number + 1 for number in range(20)}
test_4 = tuple(range(22))

print("test_1\n", prime_indices(test_1))
print("\ntest_2\n", prime_indices(test_2))
print("\ntest_3\n", prime_indices(test_3))
print("\ntest_4\n", prime_indices(test_4))
