def country_names(countries, city):
    find_country = ""
    for search_country in countries:
        if city in countries[search_country]:
            find_country += search_country
    return find_country


country_count = int(input("Количество стран: "))

questions_countries = dict()

for number in range(1, country_count + 1):
    questions = input("{} страна: ".format(number)).split()
    questions_countries[questions[0]] = questions[1:]

for number in range(1, 4):
    cities = input("\n{} город: ".format(number))
    country = country_names(questions_countries, cities)

    if len(country) != 0:
        print("Город {0} расположен в стране {1}.".format(cities, country))
    else:
        print("По городу {} данных нет.".format(cities))

# зачет!
