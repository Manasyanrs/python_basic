import itertools


position_number = list(range(10))
for code in itertools.product(position_number, repeat=4):
    print(code)

# зачет!
