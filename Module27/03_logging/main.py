import datetime
from typing import Callable, Any
import functools


# TODO дать более явное название
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
        # TODO  логирование можно сразу сделать тут

        try:
            # TODO лучше записать рещультат работы в переменную
            function(*args, **kwargs)

        except TypeError:
            # TODO и залогировать ошибку тут используя модуль logging

            # TODO знак для переноса не используем в коде
            errors += "Названые функции {function_name}\n" \
                     "Названые ошибки {errors_name}\n" \
                     "Дата и время ошибки {data_time}\n".format(
                        function_name=function.__name__,
                        errors_name=TypeError,
                        data_time=data_time)

        with open("function_errors.log", "a", encoding="utf-8") as error:
            error.write(str(errors))
        # TODO тут мы должны вернуть работу переменной полученной выше
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


#  при логирование не работает декоратор
#  а без логирование не получается обработать ошибки
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
