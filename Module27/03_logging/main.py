import datetime
from typing import Callable, Any
import functools
import logging


logging.basicConfig(filename="function_errors.log", level=logging.ERROR, )


def find_error(function: Callable) -> Any:
    """ Декаратор обработовает пераданную функцию если находит ошыбки
    то в файл function_errors.log записываются название функции и название ошибки
    Используя модуль datetime также записоваем дату и время возникновения ошибки
    :param function: Принимает на обработку итеруемый объект
    :return: None
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        data_time = datetime.datetime.now()
        print("Названые функции {function_name}\n"
              "Документация функции {function_doc}\n".format(
                function_name=function.__name__,
                function_doc=function.__doc__))
        result = None
        try:
            result = function(*args, **kwargs)
            return result
        except TypeError:
            #  обработает толко первую ошибку
            logging.exception("\nНазваные функции {function_name}\n"
                              "Названые ошибки {errors_name}\n"
                              "Дата и время ошибки {data_time}\n".format(
                                function_name=function.__name__,
                                errors_name=TypeError,
                                data_time=data_time))
        return result
        # print("Программа завершилься")

    return wrapper

# отрабатывает первую ошибку потому что мы ловим ошибку в конкретной функции и как только мы поймали в ней ошибку
# программы завершается
# поправил вам код явно рейзить не нужно да и выше результат должен возращать вот так
@find_error
def is_digit(file: Any) -> Any:
    for element in file:
        if element % 2 != 0:
            print('raise TypeError')


text_info = [0, 2, 3, "hello", 3, 8, "world", 0]

is_digit(text_info)

# зачет!
