from typing import Callable
import functools


def check_permission(arg: str) -> Callable:
    """Декаратор функци на вход получает арумент и проверяет если такой аргумент есть в списке то декорирует функцию,
    если нету то выводит на экран сообщение
    :argument
         arg: str (Передается названые аргумента)
    :raise
        У пользователя недостаточно прав, чтобы выполнить функцию + названые функции
    """
    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        try:
            if arg in user_permissions:
                return wrapper
            raise PermissionError

        except PermissionError:
            print("PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {}".format(
                function.__name__))

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """Функция выводит на экран сообщение Удаляем сайт"""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """Функция выводит на экран сообщение Добавляем комментарий"""
    print('Добавляем комментарий')


delete_site()
add_comment()
