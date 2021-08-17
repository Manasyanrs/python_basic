import os
import zipfile


def count_and_letters(file):
    result = {}
    for element, count in file.items():
        if count not in result:
            result[count] = []
            result[count].append(element)
        else:
            result[count].append(element)

    return result


def sort_file(argument):
    result = []
    for item in sorted(argument.keys()):
        result += item, argument[item]
    return result


path = os.path.abspath(os.path.join(""))
files = zipfile.ZipFile("voyna-i-mir.zip", "r")
files.extractall(path)
files.close()

english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

english = dict()
russian = dict()

a = open("voyna-i-mir.txt", "r", encoding="utf-8")

for letters in a.read():
    if letters in english_alphabet:
        if letters not in english:
            english[letters] = 1
        else:
            english[letters] += 1
    elif letters in russian_alphabet:
        if letters not in russian:
            russian[letters] = 1
        else:
            russian[letters] += 1
    else:
        pass

a.close()

russian_file = count_and_letters(russian)
english_file = count_and_letters(english)

print(sort_file(russian_file))
print(sort_file(english_file))
