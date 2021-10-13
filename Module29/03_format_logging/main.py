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

            # TODO тут у меня прорблема с выводом метода
            print("Тут метод", end=" ")
            start = time.time()
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
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    # TODO если test_sum_2 менять на @classmethod или @staticmethod то получаю ошыбку
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
