families = {
    1: {
        "Сидоров Никита": 45,
        "Сидорова Алина": 43,
        "Сидорова Палина": 20
    },

    3: {
        "сидоров Гриша": 39,
        "Петухова Палина": 40,
        "vСидоров Саша": 13,
        "Егоров Павел": 10

    },

    2: {
        "Сидоровапапова Палина": 34
    },

    4: {
        "Иванов Антон": 35,
        "Сидорова Палина": 34,
        "Сидоров Илья": 10,

        }
}
surname_question = input("Введите фамилию семьи: ").lower()
id_family = set()

result = dict()

for index, name_family in families.items():
    result[index] = {}
    for name in name_family.keys():
        surname = name.split()
        if surname_question == surname[0].lower() or surname_question + "а" == surname[0].lower():
            id_family.add(index)
            result[index][name] = families[index][name]

if len(id_family) > 0:
    print("В базе есть {family_count} семьи с фамилией {family_surname}".format(
        family_count=len(id_family),
        family_surname=surname_question.capitalize()
    ))
else:
    print("В базе нет семьи с фамилией {family_surname}".format(
        family_surname=surname_question.capitalize()
    ))

for digit in id_family:
    print("\nId семьи:\n", end=" ")
    for number, name_value in result.items():
        if digit == number:
            print(number)
            for name_surname, age in name_value.items():
                print(name_surname, age)

# зачет!
