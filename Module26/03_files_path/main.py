import os


def gen_files_path() -> list:
    for root, dirs, _ in os.walk(os.path.abspath(os.sep)):
        print(root)
        yield dirs


questions = input("Введите имя каталога: ")

gen_files = (element for element in gen_files_path())

for file in gen_files:
    if questions in file:
        break

# зачет!
