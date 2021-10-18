from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_function: Callable) -> Callable:
    """ Декоратор на вход принемает другой декоратор """
    def wrapper(*args, **kwargs):
        result = decorator_function(*args, **kwargs)
        return result
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(function: Callable, *dec_args, **dec_kwargs):
    """ Декоратор на вход принемает функцию, не именованные аргументы и именованные аргументы
     и выводит на экран сообщение (Переданные арги и кварги в декоратор: *args, **kwargs) """
    @functools.wraps(function)
    def wrapper(*func_args, **func_kwargs):
        print("Переданные арги и кварги в декоратор:", dec_args, dec_kwargs)
        result = function(*func_args, **func_kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
# TODO не пойму как передать нейминг параметров если декоратор принемает *args и **kwargs?
def decorated_function(text: str, number: int) -> None:
    """ Функция на вход принемает 2 аргумента и выводит на экран сообщение 'Привет первый аргумент и второй аргумент.
    :argument
        text: str
        number: int """

    print("Привет", text, number)


decorated_function(text="Юзер", number=101)
