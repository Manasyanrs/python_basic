class Water:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Воздух" and self.name == "Вода":
            return "{} + {} = Шторм".format(self.name, other.name)
        if other.name == "Огонь" and self.name == "Вода":
            return "{} + {} = Пар".format(self.name, other.name)
        if other.name == "Земля" and self.name == "Вода":
            return "{} + {} = Грязь".format(self.name, other.name)


class Air:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Огонь" and self.name == "Воздух":
            return "{} + {} = Молния".format(self.name, other.name)
        if other.name == "Земля" and self.name == "Воздух":
            return "{} + {} = Пыль".format(self.name, other.name)


class Fire:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if other.name == "Земля" and self.name == "Огонь":
            return "{} + {} = Лава".format(self.name, other.name)


class Earth:
    def __init__(self, name):
        self.name = name


water = Water("Вода")
air = Air("Воздух")
fire = Fire("Огонь")
earth = Earth("Земля")

storm = water + air
vapor = water + fire
dirt = water + earth
lightning = air + fire
dust = air + earth
lava = fire + earth
print(storm)
print(vapor)
print(dirt)
print(lightning)
print(dust)
print(lava)
