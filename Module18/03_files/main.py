name_file = input("Название файла: ")

if not name_file.endswith(".txt") and not name_file.endswith(".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
elif name_file[0] == "@" or name_file[0] == "№" or \
        name_file[0] == "$" or name_file[0] == "%" or \
        name_file[0] == "^" or name_file[0] == "&" or \
        name_file[0] == "*" or name_file[0] == "(" or name_file[0] == ")":
    print("Ошибка: название начинается на один из специальных символов")
else:
    print("Файл назван верно.")
