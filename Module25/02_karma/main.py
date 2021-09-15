import random


def one_day():
    return random.randint(1, 7)


exceptions = ["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"]
karma_points = 0
iterations = 0
while karma_points <= 500:
    iterations += 1
    point = one_day()
    if iterations % 10 != 0:
        karma_points += point
    else:
        with open("karma.log", "a", encoding="utf-8") as karma:
            karma.write("{}\n".format(random.choice(exceptions)))
