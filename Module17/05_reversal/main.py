text = input("Введите текст: ")
text = text[::-1]

count_h = []
for letters in range(len(text)):
    if text[letters] == "h" or text[letters] == "H":
        count_h.append(letters)

print("\nТекст в зеркальном виде", text)

if len(count_h) < 2:
    print("Количество буквы 'h' меньше двух")

elif len(count_h) == 2:
    print("Элементы между буквами 'h'", text[count_h[0] + 1:count_h[1]])

else:
    for index in range(len(count_h) - 1):
        print("Элементы между буквами 'h'", text[count_h[index] + 1:count_h[index + 1]])

# TODO сейчас при запуске слова меняются местами чего быть не должно
# TODO сделайте чтобы только менялись буквы в слова но не их расположение
# TODO Enter word: Привет h 123 как дела 54321 h это переворот!
# TODO h 12345 алед как 321
# TODO должно быть так
# TODO Привет h 321 как алед 12345 h это переворот!
