from typing import Callable


def check_permission(arg: str) -> Callable:
    def decorator(function: Callable) -> Callable:
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
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
