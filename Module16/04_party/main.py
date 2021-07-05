guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print("\nСейчас на вечеринке", len(guests), "человек:", guests)
    questions = input("Гость пришёл или ушёл? ")

    if questions == "ушёл":
        name_guests = input("Имя гостя: ")
        print("Пока, " + name_guests + "!")
        guests.remove(name_guests)

    if questions == "пришёл":
        name_guests = input("Имя гостя: ")

        if len(guests) < 6:
            print("Привет, " + name_guests + "!")
            guests.append(name_guests)
        elif len(guests) == 0:
            print("Все гости ушли")
        else:
            print("Прости, " + name_guests + " , но мест нет")

    if questions == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break
