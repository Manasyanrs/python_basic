import math


class Circle:
    def __init__(self, radius_x=1, radius_y=1):
        self.radius_x = radius_x
        self.radius_y = radius_y

    def square(self):
        if self.radius_y == 1:
            print("Площадь окружности = {:.2f}\n".format(2 * math.pi * self.radius_x ** 2))
        else:
            print("Площадь первой окружности = {:.2f}".format(2 * math.pi * self.radius_x ** 2))
            print("Площадь втарой окружности = {:.2f}\n".format(2 * math.pi * self.radius_y ** 2))

    def perimeter(self):
        if self.radius_y == 1:
            print("Периметр окружности = {:.2f}\n".format(2 * math.pi * self.radius_x))
        else:
            print("Периметр первой окружности = {:.2f}".format(2 * math.pi * self.radius_x))
            print("Периметр втарой окружности = {:.2f}\n".format(2 * math.pi * self.radius_y))

    def increase(self, n_times_radius_x, n_times_radius_y=1):
        self.radius_x *= n_times_radius_x
        self.radius_y *= n_times_radius_y
        if self.radius_y == 1:
            print("Радиус окружности = {:.2f}\n".format(self.radius_x))
        else:
            print("Радиус первогой окружности = {:.2f}".format(self.radius_x))
            print("Радиус втрого окружности = {:.2f}\n".format(self.radius_y))

    def intersect(self):
        if self.radius_x == self.radius_y:
            print("Окружность пересекается")
        elif self.radius_y == 1:
            print("Окружность не пересекается с другими поскольку она одна на координатной плоскости")
        else:
            print("Окружность не пересекается")


test = Circle(2)
test.square()
test.perimeter()
test.increase(2)
test.perimeter()
test.intersect()
