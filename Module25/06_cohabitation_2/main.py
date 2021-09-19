class House:
    """
        Дом характеризуется:
        - кол-во еды в холодильнике (в начале - 50)
        - кол-во денег в тумбочке (в начале - 100)
        - еда для кота (в начале 30)
        - кол-во грязи (в начале - 0)
    """

    __human_food = 50
    __many = 100
    __pet_food = 30
    __amount_of_dirt = 0

    def get_fridge(self):
        return self.__human_food

    def get_bedside_table_with_money(self):
        return self.__many

    def get_pet_food(self):
        return self.__pet_food

    def get_dirt(self):
        return self.__amount_of_dirt

    def set_fridge(self, food):
        House.__human_food += food
        if self.__human_food < 0:
            print("Еди мало надо купить продукты")

    def set_bedside_table_with_money(self, many):
        House.__many += many
        if self.__many < 0:
            print("Денег на счету {}".format(self.__many))

    def set_pet_food(self, food):
        if self.__pet_food < 0:
            print("Кот умер от голода")
        else:
            House.__pet_food += food

    @staticmethod
    def set_dirt(count_dirt):
        House.__amount_of_dirt += count_dirt


class Human:
    """
    Любое действие кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
    У людей есть имя,
    степень сытости (в начале - 30) и
    степень счастья (в начале - 100).
    Все люди могут гладить кота (+5 к счастью)
    Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
    """
    __degree_of_satiety = 30
    __degree_of_happiness = 100

    def __init__(self, name):
        self.__name = name
        self.house = House()

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__degree_of_satiety

    def get_happiness(self):
        return self.__degree_of_happiness

    @staticmethod
    def pat_the_pet():
        Human.__degree_of_happiness += 5
        Human.__degree_of_satiety -= 10

    def eat(self):
        self.house.set_fridge(-10)
        Human.__degree_of_satiety += 10

    def set_satiety(self, count_satiety):
        if self.__degree_of_satiety > 0:
            Human.__degree_of_satiety += count_satiety
        else:
            print("Человек умер от голода")

    def set_happiness(self, count_happiness):
        if self.__degree_of_happiness != 0:
            Human.__degree_of_happiness += count_happiness
        else:
            print("Человек умиер от депрессии")


class Husband(Human):
    """
        Любое действие кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
        Муж может:
        - есть,
        - играть,
            Степень счастья растет: у мужа от игры в компьютер (на 20),
        - ходить на работу,
            Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
    """

    def play(self):
        self.set_satiety(-10)
        self.set_happiness(20)

    def work(self):
        self.set_satiety(-10)
        self.house.set_bedside_table_with_money(150)


class Wife(Human):
    """
    Любое действие кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
    Жена может:
    - есть,
    - покупать продукты,
        Еда стоит 10 денег 10 единиц еды.
        Еда для кота тоже покупается: за 10 денег 10 еды.
    - покупать шубу,
         Шуба стоит 350 единиц.
         От покупки шубы у жены степень счастья растет:  (на 60, но шуба дорогая)
    - убираться в доме,
        За одну уборку жена может убирать до 100 единиц грязи.
    """
    __total_eat_food = 50
    __count_coat = 0

    def get_coat(self):
        return self.__count_coat

    def get_total_food(self):
        return self.__total_eat_food

    def go_shop(self):
        self.set_satiety(-10)
        self.to_buy_food()
        self.buy_a_fur_coat()

        if self.house.get_pet_food() < 20:
            self.house.set_pet_food(30)
            self.house.set_bedside_table_with_money(-30)

    def to_buy_food(self):
        self.house.set_bedside_table_with_money(-50)
        self.house.set_fridge(50)
        self.__total_eat_food += 50

    def buy_a_fur_coat(self):
        if self.house.get_bedside_table_with_money() - 50 >= 350:
            self.house.set_bedside_table_with_money(-350)
            self.set_happiness(60)
            self.__count_coat += 1

    def get_clean_the_house(self):
        self.set_satiety(-10)
        self.house.set_dirt(-100)


class Cat:
    """
    У кота есть имя и степень сытости (в начале - 30)
    Любое действие кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
    Кот может:
    - есть,
        Кот кушает максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
    - спать,
        Уменьшать степень сытости на 10 пунктов
    - драть обои
        Если кот дерет обои, то грязи тоже становится больше на 5 пунктов
    """
    __degree_of_satiety_cat = 30

    def __init__(self, name):
        self.__name = name
        self.house = House()

    def eat(self):
        self.__degree_of_satiety_cat += 2 * 10
        self.house.set_pet_food(-10)

    def slip(self):
        self.__degree_of_satiety_cat -= 10

    def play(self):
        self.__degree_of_satiety_cat -= 10
        self.house.set_dirt(5)

    def get_degree(self):
        return self.__degree_of_satiety_cat


house = House()
husband = Husband("Jack")
wife = Wife("Tina")
cat = Cat("Bars")

count_day = 0
flag = True

while flag:

    house.set_dirt(5)
    for one_third in range(3):
        husband.eat()
        wife.eat()
        cat.eat()
        if one_third == 0:
            husband.pat_the_pet()
            husband.work()

        cat.play()
        cat.slip()

        if house.get_fridge() < 20:
            wife.go_shop()

    if house.get_dirt() > 90:
        wife.set_happiness(-10)
        husband.set_happiness(-10)
        if house.get_dirt() == 100:
            wife.get_clean_the_house()

    if cat.house.get_pet_food() < 20:
        wife.pat_the_pet()
        wife.go_shop()

    husband.play()

    if count_day == 365:
        print("\nИтоги жизни за год:\nЗаработано денег {}\nСьедено еды {} единиц\nКуплено шуб {} штук".format(
            husband.house.get_bedside_table_with_money(), wife.get_total_food(), wife.get_coat()
        ))

        flag = False

    count_day += 1
