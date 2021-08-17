text = open("zen.txt", "r")

text_line = text.readlines()
text_line[-1] += "\n"

for line in range(1, len(text_line) + 1):
    print(text_line[-line], end="")

text.close()
