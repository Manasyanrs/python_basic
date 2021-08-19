winners = []

first_text = open("first_tour.txt", "r")
print("Содержимое файла {}".format(first_text.name))
for element in first_text.readlines():
    print(element, end="")
    element = element.split()
    if len(element) > 1 and int(element[2]) > 80:
        winners.append(element)
first_text.close()

player_points = []
for information in winners:
    player_points.append("{} {} {}".format(information[1][0], information[0], information[2]))

player_points = (sorted(player_points, reverse=True))
count_players = len(player_points)

second_text = open("second_tour.txt", "w")
second_text.write(str(count_players) + "\n")
number = 0
for info in player_points:
    number += 1
    second_text.write("{}) {}\n".format(number, info))
second_text.close()

print()

info_second_text = open("second_tour.txt", "r")
print("\nСодержимое файла", info_second_text.name)
print(info_second_text.read())
info_second_text.close()
