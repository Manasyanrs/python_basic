import random


class Parent:
    parent_age = 0
    childes = []

    def __init__(self, father_name, father_age, mather_name, mather_age):
        self.father_name = father_name
        self.father_age = father_age
        self.mather_name = mather_name
        self.mather_age = mather_age
        age = min(father_age, mather_age)
        self.parent_age += age
        Child.hungry += 1

    def information(self):
        if len(self.childes) == 0:
            print("Отец\nИмя {}\nВозраст {}\n\nМать\nИмя {}\nВозраст {}\n{}".format(
                self.father_name, self.father_age, self.mather_name, self.mather_age, "\nУ семии детей нету"))
        else:
            print("Отец\nИмя {}\nВозраст {}\n\nМать\nИмя {}\nВозраст {}\n\nСписок детей\n".format(
                self.father_name, self.father_age, self.mather_name, self.mather_age))
            print("{:10} {:5}".format("Имя", "возрост"))
            for child in self.childes:
                child = child.split()
                print("{:10} {:5}".format(child[1], child[-1]))

    def calm_child(self, name_child):
        for info in self.childes:
            if name_child in info:
                print(name_child, "Успакойся!\n")
                break
            else:
                print("Упс у Вас нету ребенка с таким именем:\n")

    def feed_the_baby(self):
        Child.hungry += 1
        print("Ребенок поел.\n")


class Child:
    hunger_state = {0: "Да я хочу есть", 1: "Нет я не хочу есть", 2: "Я сыт"}
    state = "спит", "играет", "учится", "гуляет"
    hungry = 0

    def __init__(self, child_name, child_age):
        self.child_name = child_name
        self.child_age = child_age
        if self.child_age > parent.parent_age - 16:
            print("Родитель должен быть старше над ребенком хотя би на 16 лет\n")

        else:
            Parent.childes.append("Имя: {} \nвозрост: {}\n".format(self.child_name, self.child_age))

    def child_hungry_state(self):
        if self.hungry < 2:
            print("\n{} будешь кушать?\n{}\n".format(self.child_name, self.hunger_state[self.hungry]))

        elif self.hungry == 2:
            print(self.child_name, self.hunger_state[self.hungry])

    def state_of_calm(self):
        result = random.choice(self.state)
        print("{} сейчас {}".format(self.child_name, result))


parent = Parent("Ivan", 29, "Tina", 28)
tim = Child("Tim", 15)
bob = Child("Bob", 12)
sem = Child("Sem", 9)

parent.calm_child("Bob")

parent.information()
sem.child_hungry_state()
bob.child_hungry_state()

parent.feed_the_baby()

sem.child_hungry_state()
parent.feed_the_baby()

bob.state_of_calm()
