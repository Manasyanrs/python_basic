def is_palindrome(text):
    end_letters = -1
    for letters in range(len(text)):
        if text[letters] == text[end_letters]:
            end_letters -= 1
            if abs(end_letters) == len(text):
                return "Yes"

        else:
            return "No"


step = 0
test_word = input("Введите строку: ").lower()

new_words = []
palindrome_word = 0
palindrome = is_palindrome(test_word)

if palindrome == "Yes":
    print("Слово является палиндромом")

else:
    for letter in range(len(test_word) - 1):
        step += 1
        if letter < 1:
            new_words.append(test_word[step:] + test_word[letter])
        else:
            new_words.append(test_word[step:] + test_word[:step])

    for word in new_words:
        palindrome = is_palindrome(word)

        if palindrome == "Yes":
            palindrome_word += 1
            break

    if palindrome_word == 1:
        print("Можно сделать палиндромом")
    else:
        print("Нельзя сделать палиндромом")
