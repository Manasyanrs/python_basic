text = input("Введите текст: ")

vowels_letters = "ауоыиэяюе"
results = [letters for letters in text for vowels in vowels_letters if vowels == letters]

print("Список гласных букв:", results)
print("Длина списка:", len(results))
