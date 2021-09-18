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
    karma = random.randint(1, 7)
    error = random.randint(1, 10)

    if error != 1:
        return karma

    else:
        # TODO далее условие если еррор равен 13 то мы choice выбираем случайное исключение из списка
        # TODO и его рейзим как объект используя ()
        result = random.choice(file)
        # TODO не понимаю как можно к result-у исползовать ()
        raise result


exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
karma_points = 0
errors = []
while karma_points <= 500:
    point = one_day(exceptions)

    if isinstance(point, int):
        karma_points += point

    else:
        # TODO не пойму что вернет point чтобы реолизовать блок else
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
