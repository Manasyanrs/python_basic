from typing import List


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


new_floats: List[float] = list(map(lambda element: round(element ** 3, 3), floats))
print("Число из списка floats возводится в третью степень и округляется до трёх знаков после запятой\n", new_floats)

new_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
print("\nИмена из списка names в которых есть хотя бы 5 букв\n", new_names)

new_numbers: List[int] = sum(map(lambda digit: digit, numbers))
print("\nПроизведение всех чисел из списка numbers = {}".format(new_numbers))
