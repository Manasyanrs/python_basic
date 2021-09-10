import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def battle(self):
        self.health -= 20
        return self.life()

    def life(self):
        if self.health > 0:
            return True
        else:
            return False


warrior_1 = Warrior("Thanos")
warrior_2 = Warrior("Hulk")
print("Игра началась\n")
flag = True
while flag:
    hit = random.randint(1, 2)
    if hit == 1:
        flag = warrior_2.battle()
        print("Атаковал воин {} здоровья = {}% у противника осталось {}% здоровья".format(
            warrior_1.name, warrior_1.health, warrior_2.health
        ))

    else:
        flag = warrior_1.battle()
        print("Атаковал воин {} здоровья = {}% у противника осталось {}% здоровья".format(
            warrior_2.name, warrior_2.health, warrior_1.health
        ))

if warrior_1.health > 0:
    print("\nПобедил воин {}".format(warrior_1.name))
else:
    print("\nПобедил воин {}".format(warrior_2.name))
