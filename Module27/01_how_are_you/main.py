from typing import Callable, Any
import functools


def how_are_you(function: Callable) -> Any:
    """Декоратор спрашивает у пользователя “Как дела?” и вне зависимости от его ответа,
    отвечает “А у меня не очень! Ладно, держи свою функцию.”
    и только потом запускает саму функцию """

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print("Как дела?", end=" ")
        input()
        print("А у меня не очень! Ладно, держи свою функцию.")
        return function(*args, **kwargs)
    return wrapper


@how_are_you
def factorial(digit: int) -> str:
    """
    Функция возврашает факториал вводимого числа
    :param digit: число для факториала
    :return: str
    """
    result = 1
    for element in range(2, digit + 1):
        result *= element
    return "Факториал числа {digit} = {result}".format(digit=digit, result=result)


print(factorial(5))
