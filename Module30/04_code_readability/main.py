import math
from collections import Counter

prime_numbers = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(math.sqrt(x)) + 1))), range(2, 1000)))
print(prime_numbers)

prime_numbers_1 = [unique_element for unique_element, repeatable_element in Counter([digit for digit in range(1000)
                                                                                     if digit != 0 and digit != 1
                                                                                     for element in range(2, digit + 1)
                                                                                     if digit % element == 0]).items()
                   if repeatable_element == 1]
print(prime_numbers_1)

# TODO по дз потребовался
# TODO 1. “однострочным” кодом, без объявления дополнительных функций;
# TODO 2. обычным, “своим” кодом, который покажется вам наиболее красивым.
# TODO такой вариант по мне еще лучше и понятнее
prime_numbers_2: list = []
temporary_variable: int = 0

for digit in range(1000):
    if digit != 0 and digit != 1:
        for element in range(2, digit + 1):
            if digit % element == 0:
                temporary_variable += 1
        if temporary_variable <= 1:
            prime_numbers_2.append(digit)
            temporary_variable = 0
        else:
            temporary_variable = 0

print(prime_numbers_2)
