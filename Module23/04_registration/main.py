def is_true_protocols(file):
    try:
        if len(file) == 0:
            raise IndexError
        if not file[0].isalpha():
            raise NameError
        if "@" not in file[1] or "." not in file[1]:
            raise SyntaxError
        if not file[2].isdigit():
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
        return file


with open("registrations.txt", "r", encoding="utf-8") as registration_protocols:
    for protocol in registration_protocols.readlines():
        result = is_true_protocols(protocol.split())
        if result:
            with open("registrations_good.log", "a", encoding="utf-8") as good_log:
                good_log.write(str(protocol))
        else:
            with open("registrations_bad.log", "a", encoding="utf-8") as bad_log:
                bad_log.write(str(protocol))
