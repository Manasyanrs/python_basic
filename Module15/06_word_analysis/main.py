def count_unique_letters(word):
    count_letters = 0
    for letters in word:
        total = 0
        for element in word:
            if letters == element:
                total += 1
        if total == 1:
            count_letters += total

    print("\nКол-во уникальных букв:", count_letters)


questions = input("Введите слово: ")

count_unique_letters(questions)
