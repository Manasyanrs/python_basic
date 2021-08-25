name = input("Введите имя: ")
print("1. Посмотреть текущий текст чата")
print("2. Отправить сообщение  (затем вводит сообщение)")

while True:
    questions = input("Ведите действе 1 или 2: ")
    if questions == "1":
        try:
            with open("message.txt") as text:
                result = text.read()
                if len(result.split()) == 0:
                    raise Warning
                else:
                    print(result)
        except (Warning, FileNotFoundError):
            print("Чат пустой")

    if questions == "2":
        write_massage = input("Введите сообщение: ")
        with open("message.txt", "a") as text:
            text.write("{} \n".format(write_massage))
