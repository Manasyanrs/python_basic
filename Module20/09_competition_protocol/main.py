question = int(input("Сколько записей вносится в протокол? "))
print("Записи (результат и имя):")
tournament = []

for number in range(1, question + 1):
    member = input("{} запись: ".format(number)).split()
    tournament.append({member[0]: member[1]})

points_participant = []
for participant in tournament:
    points_participant += [int(point) for point in participant.keys()]

points_participant = [str(point) for point in sorted(points_participant)]

point_gamer = []
name_gamer = []
place_the_pedestal = 1

while place_the_pedestal != 4:
    for participant_tournament in tournament:
        for player_points, player_name in participant_tournament.items():
            if points_participant[-place_the_pedestal] == player_points:
                if player_name not in name_gamer:
                    point_gamer.append(player_points)
                    name_gamer.append(player_name)
        if len(point_gamer) == place_the_pedestal:
            place_the_pedestal += 1
            break

print("\nИтоги соревнований:")
for number_participants in range(1, 4):
    print("{number} место. {name_participants} ({point_participants})".format(
        number=number_participants,
        name_participants=name_gamer[number_participants - 1],
        point_participants=point_gamer[number_participants - 1]
    ))
