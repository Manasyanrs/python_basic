from typing import Callable, Any
import functools


def decoration(function: Callable) -> Any:
    """ Декаратор обработовает пераданную функцию и выводит её имя (вместе со всеми передаваемыми аргументами)/
    И после этого выводится результат её выполнения
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        result = function(*args, **kwargs)
        human_name = ""

        for name in args:
            human_name = name

        if not kwargs:
            print("Вызывается {} ('{}')".format(function.__name__, human_name))
            print("{} вернула значение {}".format(function.__name__, result))
            print(result)
            print()

        if args and kwargs:
            for key, value in kwargs.items():
                information = list(args)
                information.append("{} = {}".format(key, value))

                print("Вызывается {} {}".format(function.__name__, tuple(information)))
                if value >= 100:
                    print("{} вернула значение {}".format(function.__name__, result))
                    print("Ого, {}! Тебе уже 100 лет, ты вырос!".format(human_name))
                    print()
                else:
                    print("{} вернула значение {}".format(function.__name__, result))
                    print(result)
                    print()

        if len(kwargs) == 2:
            kwargs_result = []
            for names, items in kwargs.items():
                kwargs_result.append("{} = {}".format(names, items))
            print("Вызывается {} {}".format(function.__name__, tuple(kwargs_result)))
            print("{} вернула значение {}".format(function.__name__, result))
            print(result)
            print()

    return wrapper


@decoration
def greeting(name: str, age=None) -> str:
    """ Функция на вход принимает имя, возрост и возврашает некоторое информацию
        :param age: возрост
        :rtype: int
        :param name: имя
        :rtype: str

        """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
