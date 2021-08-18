alphabet = "abcdefghijklmnopqrstuvwxyz"
file = open("text.txt", "r")
print("Содержимое файла", file.name)
text = file.read().lower()
print(text)
count_elements = 0
text_letters = ""
maximum_letters = ""
for element in text:
    if element in alphabet:
        count_elements += 1
        if text.count(element) > 1:
            if element not in maximum_letters:
                maximum_letters += element
        else:
            text_letters += element

text_letters = sorted(text_letters)
maximum_letters = sorted(maximum_letters)
total_letters = maximum_letters + text_letters

result = ""
for letter in total_letters:
    analysis_frequency = text.count(letter) / count_elements
    if letter not in result:
        result += letter + " {:0.3f} \n".format(analysis_frequency)

file.close()

second_file = open("analysis.txt", "w")
second_file.write(result)
second_file.close()

total_result = open("analysis.txt", "r")
print("\nСодержимое файла", total_result.name)
print(total_result.read())
total_result.close()

# зачет!
