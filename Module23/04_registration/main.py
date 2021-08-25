
# TODO функции не должно быть дублирующей ся части кода
# TODO with open только один раз
# TODO пусть функция принимает еще имя файла для записи
def write_protocols(flag, result):
    if flag:
        with open("registrations_bad.log", "a", encoding="utf-8") as bad_log:
            bad_log.write(str(result))
    else:
        with open("registrations_good.log", "a", encoding="utf-8") as good_log:
            good_log.write(str(result))


with open("registrations.txt", "r", encoding="utf-8") as registration_protocols:
    for protocol in registration_protocols.readlines():
        file = protocol.split()
        try:
            if len(file) == 0:
                write_protocols(True, protocol)
                raise IndexError
            if not file[0].isalpha():
                write_protocols(True, protocol)
                raise NameError
            if "@" not in file[1] or "." not in file[1]:
                write_protocols(True, protocol)
                raise SyntaxError
            if 10 > int(file[2]) or int(file[2]) > 99:
                write_protocols(True, protocol)
                raise ValueError

        except IndexError:
            print("НЕ присутствуют все три поля:")
        except NameError:
            print("Поле имени содержит НЕ только буквы:")
        except SyntaxError:
            print("Поле емейл НЕ содержит @ и .(точку):")
        except ValueError:
            print("Поле возраст НЕ является числом от 10 до 99:")
        else:
            write_protocols(False, protocol)

# TODO вам нужно сделать так функцию как в прошлом модуле оставить и из нее только вынести часть с try except
# TODO в цикл while
# TODO в функции будите рейзить
# TODO а в цикле while ловить
