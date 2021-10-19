from typing import Callable
import datetime
import time
import functools


def log_method(time_format: str, cls_name: str) -> Callable:
    """Декоратор. Выводит имена класса, метода, время запуска и время его работы."""

    form_time = ""
    for element in time_format:
        if element.isalpha():
            form_time += element.join("%")
        form_time += element
    now = datetime.datetime.now()
    total_result = now.strftime(form_time)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("- Запускается {}.{}. Дата и время запуска: {}".format(
                cls_name, func.__name__, total_result))

            start = time.time()
            print("Тут метод")
            result = func(*args, **kwargs)

            end = time.time() - start

            print("- Завершение {}.{}, время работы = {:.3f}s".format(cls_name, func.__name__, end))
            return result

        return wrapper
    return decorator


def log_methods(time_format: str) -> Callable:
    """ Декоратор. Применяет декоратор log_method ко всем методам класса. """
    def wrapped(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                method = getattr(cls, i_method)
                decorated_method = log_method(time_format, cls.__name__)(method)
                setattr(cls, i_method, decorated_method)
        return cls
    return wrapped


@log_methods("b d Y - H:M:S")
class Alfa:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class Betta(Alfa):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


test = Betta()
test.test_sum_1()
test.test_sum_2()

# TODO по примеру так

#  - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
#  - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
#  Тут метод test_sum_1"""
# TODO а у меня выходит
#  - Запускается B.test_sum_1. Дата и время запуска: Oct 18 2021 - 17:20:22
# Тут метод
# - Запускается A.test_sum_1. Дата и время запуска: Oct 18 2021 - 17:20:22
# Тут метод
# test sum 1

# TODO по другому у меня никак не получается решить данную зодачу
