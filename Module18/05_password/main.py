while True:
    password = input("Придумайте пароль: ")
    digit = 0
    upper_letters = 0

    for element in password:
        if element.isdigit():
            digit += 1
        elif element.isupper():
            upper_letters += 1

    if len(password) < 8:
        print("Пароль должен состоять минимум из 8 символов")
    elif digit < 3:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    elif upper_letters < 1:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        print("Это надёжный пароль!")
        break

# зачет!
