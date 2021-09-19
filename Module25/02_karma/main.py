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


exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]


def one_day():
    karma = random.randint(1, 7)
    error = random.randint(1, 13)

    if error == 13:
        exception = random.choice(exceptions)
        raise exception()

    return karma


karma_points = 0
errors = []
while karma_points <= 500:
    try:
        karma_points += one_day()

    except KillError:
        errors.append("KillError")
    except DrunkError:
        errors.append("DrunkError")
    except CarCrashError:
        errors.append("CarCrashError")
    except GluttonyError:
        errors.append("GluttonyError")
    except DepressionError:
        errors.append("DepressionError")

with open("karma.log", "w", encoding="utf-8") as karma:
    karma.write("{}".format(errors))

# зачет!
