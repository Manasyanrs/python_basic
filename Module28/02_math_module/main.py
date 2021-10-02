import math


class MyMath:

    @classmethod
    def circumference(cls, radius: int) -> int or float:
        return 2 * math.pi * radius

    @classmethod
    def area_circle(cls, radius: int) -> int or float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, radius: int) -> int or float:
        return radius ** 3

    @classmethod
    def surface_area_sphere(cls, radius: int) -> int or float:
        return 4 * math.pi * radius ** 2


circle_len = MyMath.circumference(radius=5)
print("Длина окружности = {}".format(circle_len))
area_circle = MyMath.area_circle(radius=6)
print("Площадь окружности = {}".format(area_circle))
cube_volume = MyMath.cube_volume(radius=6)
print("Объём куба = {}".format(cube_volume))
area_sphere = MyMath.surface_area_sphere(radius=6)
print("Площадь поверхности сферы = {}".format(area_sphere))
