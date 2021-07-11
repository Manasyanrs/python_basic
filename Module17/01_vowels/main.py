text = input("Введите текст: ")

vowels = [letters for letters in text if letters == "а" or
          letters == "у" or letters == "о" or letters == "ы" or
          letters == "и" or letters == "э" or
          letters == "я" or letters == "ю" or letters == "е"]

print("Список гласных букв:", vowels)
print("Длина списка:", len(vowels))
