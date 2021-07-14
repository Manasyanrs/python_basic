text = input("Введите текст: ")

vowels_letters = "ауоыиэяюе"
results = [letters for letters in text for vowels in vowels_letters if vowels == letters]
count_symbols = len(results)
print("Список гласных букв:", results)
print("Длина списка:", count_symbols)
