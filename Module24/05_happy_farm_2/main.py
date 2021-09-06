class Potato:
    status = {0: "Отсуствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, number_garden):
        self.number_garden = number_garden
        self.stage_of_maturity = 0

    def information(self):
        print("{} Грядка по зрелости {}".format(self.number_garden, self.status[self.stage_of_maturity]))

    def grow(self):
        if self.stage_of_maturity < 3:
            self.stage_of_maturity += 1
            return True
        elif self.stage_of_maturity == 3:
            return False


class PotatoGarden:
    def __init__(self, count_potato_garden):
        self.potatoes = [Potato(number_garden) for number_garden in range(1, count_potato_garden + 1)]

    def all_potatoes(self):
        if not all([potato.grow() for potato in self.potatoes]):
            return False
        else:
            return True


class Gardner:
    def __init__(self, name_gardner, plant_bed):
        self.name = name_gardner
        self.plant_bed = plant_bed  # Грядка с растением
        self.garden = PotatoGarden(self.plant_bed)

    def garden_care(self):  # Ухаживать за грядкой
        self.harvest()

    def harvest(self):  # Собирать урожай
        if not self.garden.all_potatoes():
            print("\nВся картошка созрела нужно собирать урожай")
        else:
            print("\nКартошка еще не созрела нужно еще ухаживать за грядкой")


gardner = Gardner("Pedro", 3)
gardner.garden_care()
