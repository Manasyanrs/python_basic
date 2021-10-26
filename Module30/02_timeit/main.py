import timeit


version_1: float = timeit.timeit('["".join(str(i) for i in range(100))]', number=10000)
print("Время работы version_list_comprehensions = {} секунд(ы).".format(version_1))

version_2: float = timeit.timeit('"".join(map(str, range(100)))', number=10000)
print("Время работы version_func_map = {} секунд(ы).".format(version_2))

# зачет!
