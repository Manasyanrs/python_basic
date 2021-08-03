number_word_pairs = int(input("Введите количество пар слов: "))

word_pairs_dictionary = dict()

for number in range(1, number_word_pairs + 1):
    words = input("{} пара  через '-': ".format(number)).split("-")
    word_pairs = [pairs for pairs in words]
    if word_pairs[0] not in word_pairs_dictionary:
        word_pairs_dictionary[word_pairs[0]] = word_pairs[1]
print()
for _ in range(2):
    synonym = input("Введите слово: ").lower()
    count = 0
    for element in word_pairs_dictionary:
        if synonym in word_pairs_dictionary[element].lower():
            print("Синоним:", element)
            count += 1
            break
    if count == 0:
        print("Такого слова в словаре нет.")
