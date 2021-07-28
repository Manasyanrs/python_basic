text = input("Сообщение: ").split()

results = ""
temporary_variable_1 = ""
temporary_variable_2 = ""
count_element = 0
for words in text:
    if words.isalpha():
        results += words[::-1] + " "
    else:
        for element in words:
            count_element += 1
            if element.isalpha():
                temporary_variable_1 += element
                if len(words) == count_element:
                    temporary_variable_2 += temporary_variable_1[::-1]
                    results += temporary_variable_2 + " "
                    temporary_variable_1 = temporary_variable_2 = ""
                    count_element = 0
            else:
                temporary_variable_2 += temporary_variable_1[::-1]
                temporary_variable_2 += element
                temporary_variable_1 = ""
                if len(words) == count_element:
                    temporary_variable_2 += temporary_variable_1[::-1]
                    results += temporary_variable_2 + " "
                    temporary_variable_1 = temporary_variable_2 = ""
                    count_element = 0

print("Новое сообщение:", results)
