class Property:
    # TODO не даем переменной название class
    __class_name = "имущество"

    def __init__(self, means, worth):
        self.means = means
        self.worth = worth

    def get_class_name(self):
        return self.__class_name

    def tax(self):
        percent = self.worth * 1 / 100
        tax_property = self.worth * percent / 100
        return tax_property

    def __str__(self):
        if self.tax() > self.means:
            lacks = self.tax() - self.means
            return "Налог на {} {} руб. для оплаты не хватает {} руб.".format(self.get_class_name(), self.tax(), lacks)

        else:
            return "Налог на {} {} руб. для оплаты налога денег хватает.".format(self.get_class_name(), self.tax())


class Apartment(Property):
    __class_name = "квартиру"

    def tax(self):
        percent = self.worth * 1 / 1000
        tax_property = self.worth * percent / 100
        return tax_property

    def get_class_name(self):
        return self.__class_name


class Car(Property):
    __class_name = "машину"

    def tax(self):
        percent = self.worth * 1 / 200
        tax_property = self.worth * percent / 100
        return tax_property

    def get_class_name(self):
        return self.__class_name


class CountryHouse(Property):
    __class_name = "дачу"

    def tax(self):
        percent = self.worth * 1 / 500
        tax_property = self.worth * percent / 100
        return tax_property

    def get_class_name(self):
        return self.__class_name


car = Car(means=3500, worth=5700)
print(car)
