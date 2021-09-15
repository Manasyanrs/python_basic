import random


def one_day():
    return random.randint(1, 7)

# TODO список с ошибками должны быть объектами названия без ()
exceptions = ["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"]
karma_points = 0
iterations = 0
while karma_points <= 500:
    iterations += 1
    point = one_day()
    if iterations % 10 != 0:
        karma_points += point
    else:
        # TODO  функцию объявить вне цикла открывать на запись один раз
        with open("karma.log", "a", encoding="utf-8") as karma:
            karma.write("{}\n".format(random.choice(exceptions)))

# TODO функция one_day() должна возвращать карму от 1 до 7 или рейзит ошибку из расчета 1 к 13
# TODO мы можем объявить 2 переменные это карма равная рендинт от 1 до 7 и
# TODO сам еррор который тоже равен рендинт от 1 до 13
# TODO далее условие если еррор равен 13 то мы choice выбираем случайное исключение из списка
# TODO и его рейзим как объект используя ()
# TODO если условие не сработало то мы ретурним карму

# TODO в цикле
# TODO ловим каждую ошибку и формируя текст ее
