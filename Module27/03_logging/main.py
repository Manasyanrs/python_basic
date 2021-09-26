import datetime
from typing import Callable, Any
import functools


def decoration(function: Callable) -> Any:
    """ Декаратор обработовает пераданную функцию если находит ошыбки
    то в файл function_errors.log записываются название функции и название ошибки
    Используя модуль datetime также записоваем дату и время возникновения ошибки
    :param function: Принимает на обработку итеруемый объект
    :return: list
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        data_time = datetime.datetime.now()
        errors = ""

        try:
            function(*args, **kwargs)

        except TypeError:
            errors += "Названые функции {function_name}\n" \
                     "Названые ошибки {errors_name}\n" \
                     "Дата и время ошибки {data_time}\n".format(
                        function_name=function.__name__,
                        errors_name=TypeError,
                        data_time=data_time)

        with open("function_errors.log", "a", encoding="utf-8") as error:
            error.write(str(errors))
        return "Программа завершилься"
    return wrapper


def logging(function: Callable) -> Any:
    """Декаратор логирует название функции и её документацию"""
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print("Названые функции {function_name}\n"
              "Документация функции {function_doc}\n"
              "Позиционные аргументы {args}\n"
              "Именованные аргументы {kwargs}".format(
                function_name=function.__name__,
                function_doc=function.__doc__,
                args=args,
                kwargs=kwargs))
    return wrapper


# TODO при логирование не работает декоратор
# TODO а без логирование не получается обработать ошибки
@logging
@decoration
def is_digit(file: Any) -> Any:
    for element in file:
        if element % 2 == 0:
            print(element)
        else:
            raise TypeError


text_info = [0, 2, 3, "hello", 3, 8, "world", 0]

is_digit(text_info)
