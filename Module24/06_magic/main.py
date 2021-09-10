class Water:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Воздух" and self.name == "Вода":
            return "{} + {} = Шторм".format(other.name, self.name)
        elif other.name == "Огонь" and self.name == "Вода":
            return "{} + {} = Пар".format(other.name, self.name)
        elif other.name == "Земля" and self.name == "Вода":
            return "{} + {} = Грязь".format(other.name, self.name)


class Air:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Огонь" and self.name == "Воздух":
            return "{} + {} = Молния".format(other.name, self.name)
        elif other.name == "Земля" and self.name == "Воздух":
            return "{} + {} = Пыль".format(other.name, self.name)


class Fire:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Земля" and self.name == "Огонь":
            return "{} + {} = Лава".format(other.name, self.name)


class Earth:
    def __init__(self, name):
        self.name = name


water = Water("Вода")
air = Air("Воздух")
fire = Fire("Огонь")
earth = Earth("Земля")

storm = water + air
print(storm)
vapor = water + fire
print(vapor)
dirt = water + earth
print(dirt)
lightning = air + fire
print(lightning)
dust = air + earth
print(dust)
lava = fire + earth
print(lava)

# TODO почему не применили метод isinstance
