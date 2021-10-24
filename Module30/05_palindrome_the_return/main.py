from collections import Counter


def can_be_poly(word: str) -> bool:
    """ Функция на вход принимает строку и проверяет можно из этой строки получить палиндром
    :argument
            word: str (передаем строку)
    :return bool
    """
    count_letters = Counter(word)
    if list(count_letters.values()).count(1) > 1:
        return False
    return True


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

# зачет!
