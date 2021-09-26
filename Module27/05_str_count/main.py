from typing import Callable, Any


def counter(function: Callable) -> Any:
    """Декоратор считающий и выводящий количество вызовов декорируемой функции."""

    def wrapper(arg: int) -> str:
        # TODO Не получается увеличить счетчик
        count = 0
        count += 1
        return "{} {}".format(function(arg), count)

    return wrapper


@counter
def even_number(digit: int) -> str:
    print(digit, end=" ")
    return "Количество вызовов декорируемой функции"


for digit in range(10):
    if digit % 2 == 0:
        print(even_number(digit))
