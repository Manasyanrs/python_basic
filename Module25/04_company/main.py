class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    __total_credit = 0

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def payment_of_wages(self):
        return


class Manager(Employee):
    __manager_salary = 13000

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def payment_of_wages(self):
        return self.__manager_salary

    def __str__(self):
        return "{} {} зарплата = {}руб.".format(self.get_name(), self.get_surname(), self.payment_of_wages())


class Agent(Employee):
    __agent_salary = 5000

    def __init__(self, name, surname, age, sales_volume):
        self.__sales_volume = sales_volume
        super().__init__(name, surname, age)

    def payment_of_wages(self):
        sales_percent = self.__sales_volume * 5 / 100
        return sales_percent + self.__agent_salary

    def __str__(self):
        return "{} {} зарплата = {}руб.".format(self.get_name(), self.get_surname(), self.payment_of_wages())


class Worker(Employee):
    def __init__(self, name, surname, age, worked_hours):
        self.worked_hours = worked_hours
        super().__init__(name, surname, age)

    def payment_of_wages(self):
        return 100 * self.worked_hours

    def __str__(self):
        return "{} {} зарплата = {}руб.".format(self.get_name(), self.get_surname(), self.payment_of_wages())


workers = [
    Manager(name="Олег", surname="Олегов", age=24),
    Manager(name="Никита", surname="Пеухов", age=26),
    Manager(name="Владимир", surname="Путин", age=32),

    Agent(name="Павел", surname="Дуров", age=34, sales_volume=73),
    Agent(name="Сергей", surname="Шойгу", age=34, sales_volume=100),
    Agent(name="Владимир", surname="Путин", age=32, sales_volume=120),

    Worker(name="Павел", surname="Воля", age=34, worked_hours=120),
    Worker(name="Джек", surname="Даниелс", age=34, worked_hours=115),
    Worker(name="Том", surname="Браун", age=34, worked_hours=105)
]

for index, person in enumerate(workers):
    if index < 3:
        if index == 0:
            print("Зарплата менеджеров\n\n{}".format(person))
        else:
            print(person)
    elif index < 6:
        if index == 3:
            print("\nЗарплата агентов\n\n{}".format(person))
        else:
            print(person)
    else:
        if index == 6:
            print("\nЗарплата рабочих\n\n{}".format(person))
        else:
            print(person)

# зачет!
