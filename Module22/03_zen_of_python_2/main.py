import os


def find_path(path, file_name):
    for element in os.listdir(path):
        path_element = os.path.join(path, element)
        if element == file_name:
            return element
        if os.path.isdir(path_element):
            results = find_path(path_element, file_name)
            if results is not None:
                return os.path.join(path, os.path.join(element, results))


this_path = os.path.abspath(os.path.basename(".."))
total_result = find_path(this_path, "zen.txt")

count_letters = 0
count_words = 0
count_line = 1

file = open(total_result, "r")
text = file.read()

for symbols in text:
    if symbols.isalpha():
        count_letters += 1

    elif symbols == " ":
        count_words += 1

    elif symbols == "\n":
        count_line += 1
        count_words += 1

file.close()

print("Количество букв Латинского алфавита в тексте:", count_letters)
print("Количество слов в тексте:", count_words)
print("Количество строк в тексте:", count_line)
