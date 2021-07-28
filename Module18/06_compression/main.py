string = input("Введите строку: ")
index = 0
count_letters = 0
iterations = 0
new_string = ""

for element in range(len(string)):
    iterations += 1
    if string[element] == string[index]:
        count_letters += 1
    else:
        new_string += string[index]
        new_string += str(count_letters)
        index = iterations - 1
        count_letters = 1

results = new_string + string[-1] + str(count_letters)

print("Закодированная строка:", results)
