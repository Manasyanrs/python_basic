from typing import Callable


def callback(arg: str) -> Callable:
    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {"//": example}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
