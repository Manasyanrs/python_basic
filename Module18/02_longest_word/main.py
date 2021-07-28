text = input("Введите строку: ").split()

word = ""
length_word = 0
for element in text:
    if len(element) > length_word:
        length_word = len(element)
        word = element

print("\nСамое длинное слово в тексте", word, "\nколичество букв в слове", word, "=", length_word)

# зачет!
