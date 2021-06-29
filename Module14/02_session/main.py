
print("Введите первую точку")
coordinates_x_1 = float(input('Введите координати первой точки X: '))
coordinates_y_1 = float(input('Введите координати первой точки Y: '))
print("\nВведите вторую точку")
coordinates_x_2 = float(input('Введите координати второй точки X: '))
coordinates_y_2 = float(input('Введите координати второй точки Y: '))

difference_x = coordinates_x_1 - coordinates_x_2
difference_y = coordinates_y_1 - coordinates_y_2
total = 0
result = coordinates_y_2 - total * coordinates_x_2
if difference_x != 0:
    division_y_x = difference_y / difference_x
    total += division_y_x
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", total, " * x + ", result)
elif difference_x == 0 and difference_y == 0:
    print("Разница двух координатов 0")
else:
    division_y_x = abs(difference_x / difference_y)
    total += division_y_x
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", total, " * x + ", result)

# TODO нужно делать уонструкцию вида if elif else
# TODO где в первых двух будем обработка если x_diff = 0 во втором y_diff = 0
# TODO при входных данных 10 20 и 10 45 ответ x = 10.0


