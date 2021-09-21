from collections.abc import Iterable


class SquareOfNumbers:
    def __init__(self, number: int) -> None:
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            result = self.counter ** 2
            self.counter += 1
            return result
        else:
            raise StopIteration


def square_of_numbers(numbers: int) -> Iterable:
    for number in range(numbers):
        yield number ** 2


questions = int(input("Введите число: "))

for digits in SquareOfNumbers(questions):
    print(digits, end=" ")

print("\n")
for digit in square_of_numbers(questions):
    print(digit, end=" ")

print("\n")
my_generator = (element ** 2 for element in range(questions))
for generator_digit in my_generator:
    print(generator_digit, end=" ")
