def write_protocols(file_name, *args):
    with open(file_name, "a", encoding="utf-8") as new_file:
        new_file.write("{}\n".format(str(args)))


good_log = "registrations_good.log"
bad_log = "registrations_bad.log"

with open("registrations.txt", "r", encoding="utf-8") as registration_protocols:
    for protocol in registration_protocols.readlines():
        file = protocol.split()
        try:
            if len(file) == 0:
                raise IndexError
            if not file[0].isalpha():
                raise NameError
            if "@" not in file[1] or "." not in file[1]:
                raise SyntaxError
            if 10 > int(file[2]) or int(file[2]) > 99:
                raise ValueError

        except IndexError:
            information = "Не присутствуют все три поля:"
            write_protocols(bad_log, protocol, information)
        except NameError:
            information = "Поле имени содержит не только буквы:"
            write_protocols(bad_log, protocol, information)
        except SyntaxError:
            information = "Поле емейл НЕ содержит @ или .(точку):"
            write_protocols(bad_log, protocol, information)
        except ValueError:
            information = "Поле возраст не является числом от 10 до 99:"
            write_protocols(bad_log, protocol, information)

        else:
            write_protocols(good_log, protocol)

print("Программа завершена")

# зачет!
