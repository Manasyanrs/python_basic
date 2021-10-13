from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = decorator_function(*args, **kwargs)
        return result
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(function: Callable, *args, **kwargs):
    @functools.wraps(function)
    def wrapper(*arg, **kwarg):
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        result = function(*arg, **kwarg)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function(text="Юзер", num=101)
