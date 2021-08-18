player_points = sorted([])
first_text = open("first_tour.txt", "r")
print("Содержимое файла", first_text.name)
number = 0
new_file = []
for element in first_text.readlines():
    print(element, end="")
    information = element.split()
    if len(information) == 1:
        number = int(information[0])
    elif int(information[2]) > number:
        player_points.append(int(information[2]))
        new_file.append(information)

player_tournament = ""
for index, point in enumerate(reversed(player_points)):
    for digit in new_file:
        if str(point) in digit:
            player_tournament += str(index + 1) + ") " + digit[1][0] + " " + digit[0] + " " + digit[2] + "\n"
first_text.close()

second_text = open("second_tour.txt", "w")
number_participant = 0
second_text.write(str(len(new_file)) + "\n")
second_text.write(player_tournament)
second_text.close()
print()
info_second_text = open("second_tour.txt", "r")
print("\nСодержимое файла", info_second_text.name)
print(info_second_text.read())
info_second_text.close()
