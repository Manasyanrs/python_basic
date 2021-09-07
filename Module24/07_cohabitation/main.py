import random


class Human:
    def __init__(self, first_name="No Name", count_human=1):
        self.first_name = first_name
        self.count_human = count_human
        self.second_name = "No name"
        self.state_of_hungry = 50
        self.house = House()

    def eat(self):  # Есть (+сытость, -еда)
        self.state_of_hungry += self.count_human * 10
        self.house.fridge()

    def work(self):  # Работать (-сытость, +деньги)
        self.state_of_hungry -= self.count_human * 10
        self.house.many += self.count_human * 10

    def play(self):  # Играть (-сытость)
        self.state_of_hungry -= self.count_human * 10

    def go_to_shop(self):  # Ходить в магазин за едой (+еда, -деньги)
        self.house.food += self.count_human * 10
        self.house.bedside_table_with_money()


class House:
    def __init__(self):
        self.food = 50
        self.many = 0

    def fridge(self):
        self.food -= 10 * person.count_human
        return self.food

    def bedside_table_with_money(self):
        self.many -= 10 * person.count_human
        return self.many


person = Human("Peter")
count_dey = 0
while True:
    count_dey += 1
    digit = random.randint(1, 6)
    if person.state_of_hungry < 0 or person.house.food < 0:
        if person.count_human == 1:
            print("{} умер от голода:".format(person.first_name))
            break
        else:
            print("{} и {} умерли от голода:".format(person.first_name, person.second_name))
            break

    elif count_dey == 365:
        if person.count_human == 1:
            print("{} осталось в живых:".format(person.first_name))
            break
        else:
            print("{} и {} остались живыми".format(person.first_name, person.second_name))
            break

    elif person.state_of_hungry < person.count_human * 20:
        person.eat()

    elif person.house.food < 10:
        person.go_to_shop()

    elif person.house.many < 50:
        person.work()

    elif digit == 1:
        person.work()

    elif digit == 2:
        person.eat()

    else:
        person.play()

# зачет!
