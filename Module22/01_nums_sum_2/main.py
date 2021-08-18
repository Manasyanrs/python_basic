text = open("numbers.txt", "r")

information_text = text.read()
print("Содержимое файла {} \n {}".format(text.name, information_text))
total_sum_digit = 0
for element in information_text.split():
    if element.isdigit():
        total_sum_digit += int(element)

text.close()

new_text = open("answer.txt", "w")
new_text.write(str(total_sum_digit))
new_text.close()
new_text = open("answer.txt", "r")
information_new_text = new_text.read()

print("Содержимое файла {} \n{}".format(new_text.name, information_new_text))
new_text.close()

# зачет!
