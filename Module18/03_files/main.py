name_file = input("Название файла: ")
symbols = "!@#$%^&*()_-+=,.:/'"

if not name_file.endswith(".txt") and not name_file.endswith(".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")

elif name_file[0] in symbols:
    print("Ошибка: название начинается на один из специальных символов")

else:
    print("Файл назван верно.")
