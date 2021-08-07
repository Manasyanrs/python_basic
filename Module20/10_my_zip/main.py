word = "abcd"
numbers = (10, 20, 30, 40)

new_variable = ()

if len(word) <= len(numbers):
    new_variable = word
else:
    new_variable = word[:len(numbers)]

result = ((element, numbers[index]) for index, element in enumerate(new_variable))
print(result)

for items in result:
    print(items)

# зачет!

