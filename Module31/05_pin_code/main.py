import itertools


# TODO используем атрибут repeat=4
# TODO range(10) выносим в переменную
for code in itertools.product(range(10), range(10), range(10), range(10)):
    print(code)
