class File:
    """
    Класс контекст менеджера File,который автоматически создаёт и открывает файл в режиме записи.
    На выходе из менеджера подавляются все исключения, связанные с файлами.

    Args:

         file_name: str (Передается имя файла)
         method: str (Передается режиме записи)

    """

    def __init__(self, file_name: str, method: str) -> None:
        self.__file_name = file_name
        self.__method = method

    def __enter__(self):
        # вот так делаем
        try:
            self.result = open(self.__file_name, self.__method, encoding="utf-8")
        except IOError:
            self.result = open(self.__file_name, "w", encoding="utf-8")
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is IOError:
            self.result.close()
            print("Программа шавершена:")
            return True
        self.result.close()


with File(file_name="example.txt", method="w") as file:
    file.write("Всем привет!")

# зачет!
