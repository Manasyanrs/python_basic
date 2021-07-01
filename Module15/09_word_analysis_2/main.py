word = input("Введите слово: ")
revers_word = word[::-1]
count_letters = 0

for letters in range(len(word)):
    if word[letters] == revers_word[letters]:
        count_letters += 1
    else:
        count_letters -= 1

if count_letters == len(word):
    print("Слово является палиндромом")

else:
    print("Слово не является палиндромом")

