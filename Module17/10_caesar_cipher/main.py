text = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
results = ""

for letters in text:
    if letters != " ":
        index = alphabet.index(letters) + step - len(alphabet)
        results += alphabet[index]

    else:
        results += " "

print("Зашифрованное сообщение:", results)
