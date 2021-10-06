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

    # TODO метод должен быть назван также как в Rectangle
    def triangle_area(self) -> int or float:
        result = 0.5 * self.base * self.height
        return result


class SquareMixin:
    # TODO  метод для нахождения площади поверхности ничего не принимает
    # TODO в методе объявляем переменную для подсчета
    # TODO далее заводим цикл по переменной в которой как мы ожидаем будет список self.surfaces:
    # TODO у объекта из списка мы вызываем метод area полученный результат записываем в переменную
    # TODO возвращаем результат

    def square(self, size_x: int or float) -> int or float:
        self.size_x = size_x
        return self.size_x ** 2


class Cube(Square, SquareMixin):
    def __init__(self, length: int or float):
        super().__init__(length)
        # TODO тут нужно определить этот список self.surfaces


class Pyramid(Square, Triangle, SquareMixin):
    def __init__(self, length: int or float):
        super().__init__(length)
        # TODO аналогично
