print("Введите координаты монетки:")
x_coordinate = float(input("X "))
y_coordinate = float(input("Y "))
radius = float(input("Введите радиус: "))

def metal_detector(coordinate_x, coordinate_y, radius):
    print()
    total_sum_x_y = coordinate_x + coordinate_y
    if radius >= total_sum_x_y >= 0:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")

metal_detector(x_coordinate, y_coordinate, radius)

# TODO применить рекомендации данные ранее
