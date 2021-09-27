from typing import Callable, Any


def counter(function: Callable) -> Any:
    """Декоратор считающий и выводящий количество вызовов декорируемой функции."""

    def wrapper(arg: int) -> str:
        # TODO так тут он равен 0
        count = 0
        # TODO а вот тут 1 и так всегда
        count += 1
        return "{} {}".format(function(arg), count)
    # TODO нужно использовать глобальный параметр функции wrapper и объявить его тут
    # TODO wrapper.count = 0

    return wrapper


@counter
def even_number(digit: int) -> str:
    print(digit, end=" ")
    return "Количество вызовов декорируемой функции"


for digit in range(10):
    if digit % 2 == 0:
        print(even_number(digit))
