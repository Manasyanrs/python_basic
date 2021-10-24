# TODO пробелма с lambda функций выводиться толко [0, 1] не пойму почему так
# TODO вед метод all возврашает True или False
prime_numbers = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, x + 1))), range(1000)))
print(prime_numbers)


# TODO По мне такой подход более понятен с точки читабельность чем в первом примере
prime_numbers_1: list = []
temporary_variable: int = 0

for digit in range(1000):
    if digit != 0 and digit != 1:
        for element in range(2, digit + 1):
            if digit % element == 0:
                temporary_variable += 1
        if temporary_variable <= 1:
            prime_numbers_1.append(digit)
            temporary_variable = 0
        else:
            temporary_variable = 0


print(prime_numbers_1)
