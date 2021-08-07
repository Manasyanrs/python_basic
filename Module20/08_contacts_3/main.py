print("Для добовленые контакта нажмите +, для поиска контакта нажмите f, для выхода нажмите 0")

phonebook = dict()

while True:
    questions = input("\nДобавить-'+', поиск-'f', выход-'0': ")
    if questions == "+":
        name = input("Введите имя и фамилию контакта: ")
        if name not in phonebook:
            phone_number = int(input("Введите номер телефона: "))
            phonebook[name] = phone_number
            print(phonebook)
        else:
            print("Контакт с таким именем уже есть")

    elif questions == "f":
        surname_contact = input("Введите фамилию контакта: ").lower()
        count = 0
        for surname in phonebook.keys():
            if surname_contact in surname.lower():
                count += 1
                print(surname, phonebook[surname])

        if count == 0:
            print("В контактах нету токого человека")

    else:
        if questions == "0":
            break
