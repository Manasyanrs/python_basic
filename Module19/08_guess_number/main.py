maximum_number = set(i for i in range(1, 1 + int(input("Введите максимальное число: "))))
numbers_in_maximum_number = 0
while True:
    questions = input("Нужное число есть среди вот этих чисел: ").lower().split()
    help_me = "".lower()
    for word in questions:
        if word == "помогите!":
            help_me += word
            break
        else:
            help_me += "Нет"
            break
    if help_me != "помогите!":
        answer = input("Ответ Артёма(Да/Нет): ").lower()
        questions_number = set(int(i) for i in questions)

        if answer == "да":
            numbers_in_maximum_number = (maximum_number.intersection(questions_number))
            print()
            if len(numbers_in_maximum_number) == 1:
                print("Артём мог загадать число:", numbers_in_maximum_number)
                break
        elif answer == "нет":
            numbers_in_maximum_number = (numbers_in_maximum_number - questions_number)
            print()
        else:
            print("Надо отвечать да или не:")

    else:
        print("Артём мог загадать следующие числа:", numbers_in_maximum_number)
        break
