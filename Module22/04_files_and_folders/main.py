import os


def search_element(file_path):
    count_directory = 0
    size_file = 0
    count_file = 0
    for path_file, count_path, files in os.walk(file_path):
        count_directory += len(count_path)
        count_file += len(files)
        for name in files:
            full_path = os.path.join(path_file, name)
            size_file += (os.path.getsize(full_path) * 1024)

    print("Размер каталога (в Кб):", size_file)
    print("Количество подкаталогов:", count_directory)
    print("Количество файлов:", count_file)


module_14_path = os.path.abspath(os.path.join("..", "..", "Module14"))
print("Результат работы программы на примере:\n{}\n".format(module_14_path))
search_element(module_14_path)
