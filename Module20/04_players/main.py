players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = []
for name, player_points in players.items():
    total = name + player_points
    result.append(total)

print(result)
