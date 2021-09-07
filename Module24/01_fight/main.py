import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    # TODO должны быть реализованы методы
    # TODO проверки себя на жизнь
    # TODO метод который ударяет себя, уменьшает жизнь на заданную величину


warrior_1 = Warrior("Thanos")
warrior_2 = Warrior("Hulk")

while True:
    if warrior_1.health > 0 and warrior_2.health > 0:
        hit = random.randint(1, 2)
        if hit == 1:
            warrior_2.health -= 20
            print("Атаковал воин {} у противника осталось {}% здоровья".format(
                warrior_1.name, warrior_2.health
            ))

        else:
            warrior_1.health -= 20
            print("Атаковал воин {} у противника осталось {}% здоровья".format(
                warrior_2.name, warrior_1.health
            ))
    else:
        if warrior_1.health > 0:
            print("\nПобедитель {}".format(warrior_1.name))
        else:
            print("\nПобедитель {}".format(warrior_2.name))
        break
