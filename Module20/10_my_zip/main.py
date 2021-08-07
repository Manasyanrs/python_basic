word = "abcd"
numbers = (10, 20, 30, 40)

# TODO тут нам нужно написать свой вариант функции zip
result = zip(word, numbers)
print(result)

new_variable = ()

if len(word) <= len(numbers):
    new_variable = word
else:
    new_variable = word[:len(numbers)]

for index, element in enumerate(new_variable):
    print((element, numbers[index]))
