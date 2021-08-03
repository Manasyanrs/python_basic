def original_dictionary(text):
    letters_and_count_letters = dict()
    for letters in text:
        if letters not in letters_and_count_letters:
            letters_and_count_letters[letters] = 1
        else:
            letters_and_count_letters[letters] += 1
    return letters_and_count_letters


def results_dictionary(my_dictionary):
    inverted_dictionary = dict()
    for items in my_dictionary:
        if my_dictionary[items] not in inverted_dictionary:
            inverted_dictionary[my_dictionary[items]] = [items]
        else:
            inverted_dictionary[my_dictionary[items]].append(items)
    return inverted_dictionary


entered_text = input("Введите текст: ")

text_dictionary = original_dictionary(entered_text)

print("Оригинальный словарь частот:")
for element in sorted(text_dictionary):
    print(element, ":", text_dictionary[element])

results = results_dictionary(text_dictionary)

print("\nИнвертированный словарь частот:")
for element in results:
    print(element, ":", results[element])
