
print("Введите первую точку")
coordinates_x_1 = float(input('Введите координати первой точки X: '))
coordinates_y_1 = float(input('Введите координати первой точки Y: '))
print("\nВведите вторую точку")
coordinates_x_2 = float(input('Введите координати второй точки X: '))
coordinates_y_2 = float(input('Введите координати второй точки Y: '))

difference_x = coordinates_x_1 - coordinates_x_2
difference_y = coordinates_y_1 - coordinates_y_2
total = 0

if difference_x == 0:
    print("x =", coordinates_x_1)
elif difference_y == 0:
    print("y =", coordinates_y_1)
else:
    total = abs(difference_x / difference_y)
    result = coordinates_y_2 - total * coordinates_x_2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", total, "* x + ", result)

# зачет!
