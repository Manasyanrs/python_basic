import os


def search_path(path, file_name):
    for files in os.listdir(path):
        full_path = os.path.join(path, files)
        if file_name == files:
            return full_path
        if os.path.isdir(full_path):
            result_search = search_path(full_path, file_name)
            if result_search is not None:
                return result_search


text = input("Введите строку: ")
file = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n").split()
tis_path = os.path.abspath(os.sep)

for name in file:
    tis_path = os.path.join(tis_path, name)

path_name = input("Введите имя файла: ") + ".txt"
result = search_path(tis_path, path_name)

if path_name not in result:
    total_result = open(path_name, "w")
    total_result.write(text)
    print("Файл успешно сохранён!")
    total_result.close()
else:
    questions = input("Вы действительно хотите перезаписать файл? ").lower()
    if questions == "да":
        rewrite = open(path_name, "w")
        rewrite.write(text)
        print("Файл успешно перезаписан!")
        rewrite.close()
    else:
        print("Это Ваш Выбор)):")
