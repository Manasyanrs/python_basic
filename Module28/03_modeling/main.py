class Rectangle:
    """Базовый класс прямоугольник
    Args:
        length: int or float (Передается длина прямоугольника)
        width: int or float (Передается ширина прямоугольника)
    """

    def __init__(self, length: int or float, width: int or float) -> None:
        self.__length = length
        self.__width = width

    def area(self):
        result = self.__length * self.__width
        return result

    def perimeter(self):
        result = 2 * self.__length + 2 * self.__width
        return result


class Square(Rectangle):
    """Базовый класс квадрат наследоваться от класса прямоугольник(Rectangle)
    Args:
        length: int or float (Передается одна сторона квадрата)
    """
    def __init__(self, length: int or float):
        super().__init__(length, length)


class Triangle:
    """Базовый класс треугольник
        Args:
            height: int or float (Передается третяя сторона треугольника)
            base: int or float (Передается высота треугольника)
        """
    def __init__(self, height: int or float, base: int or float):
        self.height = height
        self.base = base

    def area(self) -> int or float:
        result = 0.5 * self.base * self.height
        return result


class SquareMixin:
    # TODO далее заводим цикл по переменной в которой как мы ожидаем будет список self.surfaces:
    # TODO у объекта из списка мы вызываем метод area полученный результат записываем в переменную
    # TODO возвращаем результат

    def square(self):
        __total_area = 0
        for obj in surfaces:
            __total_area += obj.area(self)
        return __total_area


class Cube(Square, SquareMixin):
    def __init__(self, length: int or float):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]


class Pyramid(Square, Triangle, SquareMixin):
    def __init__(self, length: int or float):
        super().__init__(length)
        self.surfaces = [Triangle, Triangle, Triangle, Triangle]


cube = Cube(length=3)
surfaces = cube.surfaces
square3d = cube.square()
print(square3d)

pyramid = Pyramid(length=3)
surfaces = pyramid.surfaces
pyramid3d = pyramid.square()
print(pyramid3d)
