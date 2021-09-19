class Property:
    __property_name = "имущество"

    def __init__(self, means, worth):
        self.means = means
        self.worth = worth

    def get_property_name(self):
        return self.__property_name

    def tax(self):
        percent = self.worth * 1 / 100
        tax_property = self.worth * percent / 100
        return tax_property

    def __str__(self):
        if self.tax() > self.means:
            lacks = self.tax() - self.means
            return "Налог на {} {} руб. для оплаты не хватает {:.2f} руб.".format(
                self.get_property_name(), self.tax(), lacks
            )

        else:
            return "Налог на {} {} руб. для оплаты налога денег хватает.".format(
                self.get_property_name(), self.tax()
            )


class Apartment(Property):
    __property_name = "квартиру"

    def tax(self):
        percent = self.worth * 1 / 1000
        tax_property = self.worth * percent / 100
        return tax_property

    def get_property_name(self):
        return self.__property_name


class Car(Property):
    __property_name = "машину"

    def tax(self):
        percent = self.worth * 1 / 200
        tax_property = self.worth * percent / 100
        return tax_property

    def get_property_name(self):
        return self.__property_name


class CountryHouse(Property):
    __property_name = "дачу"

    def tax(self):
        percent = self.worth * 1 / 500
        tax_property = self.worth * percent / 100
        return tax_property

    def get_property_name(self):
        return self.__property_name


apartment = Apartment(means=89600, worth=115700)
print(apartment)
car = Car(means=3500, worth=5700)
print(car)
