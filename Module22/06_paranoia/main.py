upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"

text = open("text.txt", "r")
iteration = 0
result = ""
print("Содержимое файла", text.name)
for lines in text.readlines():
    print(lines, end="")
    iteration += 1
    for letters in lines:
        if letters in upper_alphabet:
            upper_letter = (upper_alphabet.index(letters) + iteration) % len(upper_alphabet)
            result += upper_alphabet[upper_letter]
        elif letters in lower_alphabet:
            lower_letter = (lower_alphabet.index(letters) + iteration) % len(lower_alphabet)
            result += lower_alphabet[lower_letter]
        else:
            result += letters
text.close()

new_file = open("cipher_text.txt", "w")
new_file.write(result)
new_file.close()

new_file = open("cipher_text.txt", "r")
print("\nСодержимое файла cipher", new_file.name)
print(new_file.read(), end="")
new_file.close()

# зачет!
