from typing import Callable
import functools


app = {}


def callback(arg: str) -> Callable:
    """Декаратор функци на вход получает арумент и заполняет пустой словарь
    по ключу arg, а значение получет функцией которую мы декорировали
    :argument
        arg: str (Передается названые аргумента)"""

    def decorator(function: Callable) -> Callable:
        app[arg] = function

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


@callback('//')
def example():
    """Функция выводит на экран сообщение 'Пример функции, которая возвращает ответ сервера'
        :return: srt """

    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
