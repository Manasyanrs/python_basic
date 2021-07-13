text = input("Введите текст: ")

vowels_letters = "ауоыиэяюе"
results = [letters for letters in text for vowels in vowels_letters if vowels == letters]

print("Список гласных букв:", results)
# TODO len тоже не используем в принте по возможности
print("Длина списка:", len(results))
