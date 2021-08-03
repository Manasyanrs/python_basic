violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

time = 0
count_songs = int(input("Сколько песен выбрать? "))
for number in range(1, count_songs + 1):
    songs_name = input("Название {} песни: ".format(number))
    time += violator_songs.get(songs_name, 0)

print("Общее время звучания песен: {:.2f} минут".format(time))

# зачет!
