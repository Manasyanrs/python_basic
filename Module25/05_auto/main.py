import random
import math


class Car:

    def __init__(self):
        self.__coordinate_x = random.random()
        self.__coordinate_y = random.random()
        self.__distance_x_y = math.sqrt(self.__coordinate_x ** 2 + self.__coordinate_y ** 2)
        self.__angle = math.asin(self.__coordinate_x / self.__distance_x_y) * 57.2958

    def move(self, distance):
        self.__angle = random.random()
        self.__coordinate_x += math.cos(self.__angle) * distance
        self.__coordinate_y += math.sin(self.__angle) * distance

    def __str__(self):
        return "\nКоординаты: {:.2f} и {:.2f} Угол: {:.2f}".format(
            self.__coordinate_x, self.__coordinate_y, self.__angle
        )


class Bus(Car):

    def __init__(self):
        self.__passengers = 0
        self.__money = 0
        super().__init__()

    def input_passengers(self, count_passengers):
        self.__passengers += count_passengers
        self.__money += count_passengers * 10

    def output_passengers(self, count_passengers):
        if self.__passengers - count_passengers < 0:
            print("Количество выходящих пассажиров больше чем в автобусе")
        elif self.__passengers - count_passengers == 0:
            self.__passengers = 0
        else:
            self.__passengers -= count_passengers

    def __str__(self):
        return super().__str__() + "\nКолечество пассажиров: {} заработанно деньг: {}".format(
            self.__passengers, self.__money
        )


car = Car()
print(car)
car.move(distance=20)
print(car)
bus = Bus()
print(bus)
bus.input_passengers(count_passengers=30)
bus.output_passengers(count_passengers=15)
print(bus)
bus.move(distance=20)
print(bus)
