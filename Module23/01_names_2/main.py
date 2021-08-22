def letter_count(file):
    count_letters = 0
    line = 0
    for name in file:
        line += 1
        count = len(name)
        if name.endswith("\n"):
            count -= 1
        try:
            count_letters += count
            if count < 3:
                raise NameError
        except NameError:
            print("Длина имени в {} строке меньше трех букв".format(line))
    print("Количество букв в файле {} штук".format(count_letters))


try:
    with open("people.txt", "r") as names:
        result = names.readlines()
        letter_count(result)
except FileNotFoundError:
    print("Файла с таким названием не сушествует")

# зачет!
