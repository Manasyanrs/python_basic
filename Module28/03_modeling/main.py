from abc import ABC, abstractmethod


class Figure2D(ABC):
    """Абстрактного базовый класса Figure2D"""

    def __init__(self, length: int or float, width: int or float,
                 height: int or float, base: int or float) -> None:
        self.length = length
        self.width = width
        self.height = height
        self.base = base

    @abstractmethod
    def perimeter(self) -> int or float:
        return self.length + self.width + self.height + self.base


class Square2D(Figure2D):
    """Базовый класс квадрат наследовается с абстрактного класса Figure2D
    Args:
        length: int or float (Передается одна сторона квадрата)
    """
    def __init__(self, length: int or float) -> None:
        super().__init__(length, length, length, length)

    def perimeter(self) -> int or float:
        return super().perimeter()

    def square(self) -> int or float:
        return self.length ** 2


class Triangle2D(Figure2D):
    """Базовый класс треугольник наследовается с абстрактного класса Figure2D
        Args:
            length: int or float (Передается первая сторона треугольника)
            width: int or float (Передается вторая сторона треугольника)
            height: int or float (Передается третяя сторона треугольника)
            base: int or float (Передается высота треугольника)
        """
    def __init__(self, length: int or float, width: int or float,
                 height: int or float, base: int or float) -> None:
        super().__init__(length, width, height, base)

    def perimeter(self) -> int or float:
        return super().perimeter() - self.height

    def triangle_square_2D(self) -> int or float:
        result = 0.5 * self.base * self.height
        return result


class Figure3D(Square2D, Triangle2D):
    __result = 0

    def square3d(self) -> int or float:
        for _ in range(6):
            self.__result += self.square()

        return self.__result

    def triangle_square3d(self) -> int or float:
        for _ in range(4):
            self.__result += self.triangle_square_2D()

        return self.__result


square = Square2D(length=3)
print("Периметр квадрата =", square.perimeter())
print("Площадь квадраат =", square.square())
print()
triangle = Triangle2D(length=4, width=3, height=4, base=8)
print("Периметр треугольника =", triangle.perimeter())
print("Площадь треугольника =", triangle.triangle_square_2D())
print()
square3d = Figure3D(4)
# TODO не получается с треугольником
triangle3d = Figure3D(3)
print("Площадь поверхности 3D квадраат", square3d.square3d())
print("Площадь поверхности 3D треугольника", triangle3d.triangle_square3d())
