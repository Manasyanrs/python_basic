import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day(file):
    # TODO karma не должна быть подчеркнута
    karma = random.randint(1, 7)
    # TODO от 1 до 13
    error = random.randint(1, 10)

    # TODO наоборот если error == 1 то мы
    if error != 1:
        # TODO через exception = random.choice(EXCEPTIONS)
        # TODO и тут зарейзим exception добавим к нему () потому что это вызов объекта Exception
        return karma
    # TODO без елсе
    else:
        # TODO далее условие если еррор равен 13 то мы choice выбираем случайное исключение из списка
        # TODO и его рейзим как объект используя ()
        result = random.choice(file)
        #  не понимаю как можно к result-у исползовать ()
        raise result


# TODO сделать константой поместить выше функции
exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

karma_points = 0
errors = []
while karma_points <= 500:
    # TODO тут должен быть блок try exception
    # TODO код ниже переписать отталкиваясь от новой one_day
    point = one_day(exceptions)

    if isinstance(point, int):
        karma_points += point

    else:
        # не пойму что вернет point чтобы реолизовать блок else
        errors.append(str(point))
        if point == KillError:
            raise KillError("KillError")
        if point == DrunkError:
            raise DrunkError("DrunkError")
        if point == CarCrashError:
            raise CarCrashError("CarCrashError")
        if point == KillError:
            raise KillError("GluttonyError")
        if point == DepressionError:
            raise DepressionError("DepressionError")


with open("karma.log", "w", encoding="utf-8") as karma:
    karma.write("{}".format(errors))
