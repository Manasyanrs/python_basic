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
        # TODO эту строку  кода нужно обернуть в конструкцию try exception
        # TODO ловить ошибку  IOError
        # TODO если ее поймали открываем файл через флаг w
        self.result = open(self.__file_name, self.__method)
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # TODO нужно проверить если exc_type is IOError
        # TODO то тогда закрываем файл и вернем True
        # TODO после условия в любом случае файл нужно закрыть
        self.result.close()
        print("Программа шавершена:")
        return True


# TODO а если влаг не указать код упадет
with File(file_name="example.txt", method="w") as file:
    file.write("Всем привет!")
