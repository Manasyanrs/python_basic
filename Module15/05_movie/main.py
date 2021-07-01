films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

love_films = []

for film in range(len(films)):
    questions = input("Название фильма: ")
    if questions in films:
        love_films.append(questions)
    else:
        print("\nФильм по запросу", questions, "не нашелся")
        break

print("Список любимых фильмов\n")
for my_film in love_films:
    print(my_film)

# зачет!
