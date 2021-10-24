import timeit
from typing import List

# version1
# TODO list в именовании не используем
version_list_comprehensions: float = timeit.timeit('["".join(str(i) for i in range(100))]', number=10000)
print("Время работы version_list_comprehensions = {} секунд(ы).".format(version_list_comprehensions))

version_func_map: float = timeit.timeit('"".join(map(str, range(100)))', number=10000)
print("Время работы version_func_map = {} секунд(ы).".format(version_func_map))


# version2
# TODO для чего эта функция ?
def result_timer(argument: object) -> None:
    """ Функция на вход принимает аргумент и выводит на экран время работы
    :type argument: object
    """
    start = timeit.timeit()
    # TODO не дописали что то
    argument
    end = timeit.timeit() - start
    print("Время работы = {} секунд(ы).".format(end))


print()
version_comprehensions: List[str] = ["".join(str(digit) for digit in range(100))]
result_timer(version_comprehensions)

version_map: str = "".join(map(str, range(100)))
result_timer(version_map)
