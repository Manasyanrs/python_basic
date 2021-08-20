import os
import zipfile


def unzip():
    path = os.path.abspath(os.path.join(""))
    files = zipfile.ZipFile("voyna-i-mir.zip", "r")
    files.extractall(path)
    files.close()


def calculator_letters():
    result = dict()
    text = open("voyna-i-mir.txt", "r", encoding="utf-8")
    for element in text.read():
        if element.isalpha():
            if element not in result:
                result[element] = 1
            else:
                result[element] += 1
    text.close()
    return result


def sort_file(file):
    numbers = sorted(file.values())
    outcome = dict()
    for digit in numbers:
        for letter, count in file.items():
            if count == digit:
                outcome[letter] = count
    return outcome


def total_result(file):
    print("|{} | {}".format("Буква", "количество"))
    for letter, count in file.items():
        print("|{}     | {}".format(letter, count))


unzip()
information = calculator_letters()
sort_result = sort_file(information)
total_result(sort_result)

# зачет!
