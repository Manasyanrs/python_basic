violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

questions = int(input("Сколько песен выбрать? "))
total_time = 0
for song in range(1, questions + 1):
    song_name = input("Название " + str(song) + " песни: ")
    # TODO сразу в заголовке цикла распаковываем и получаем имя и время из списка который придет когда мы будем
    #  итерироваться по главному списку.
    for name in violator_songs:
        if name[0] == song_name:
            total_time += name[1]

total_time = round(total_time, 2)
print("\nОбщее время звучания песен:", total_time, "минут")
