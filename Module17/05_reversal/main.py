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
