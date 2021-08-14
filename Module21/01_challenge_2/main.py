def digits_1_to_n(number):
    if number == 2:
        return 1
    elif number == 1 or number == 0:
        return 0
    else:
        print(digits_1_to_n(number - 1), end=" ")
        return number - 1


question = int(input("Введите число: "))
result = digits_1_to_n(question)
print(result)

# зачет!
