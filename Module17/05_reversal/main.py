text = input("Введите текст: ")
count_h = []

for letters in range(len(text)):
    if text[letters] == "h" or text[letters] == "H":
        count_h.append(letters)

if len(count_h) < 2:
    print("Количество буквы 'h' меньше двух")

elif len(count_h) == 2:
    results = text[count_h[0] + 1:count_h[1]]
    print("Элементы между буквами 'h'", results)
    print("Текст в зеркальном виде", results[::-1])

else:
    for index in range(len(count_h) - 1):
        maximum_h = text[count_h[index] + 1:count_h[index + 1]]
        print("Элементы между буквами 'h'", maximum_h)
        print("Текст в зеркальном виде", maximum_h[::-1])
