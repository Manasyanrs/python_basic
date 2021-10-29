import re


phone_numbers = ['9999999999', '999999-999', '99999x9999', "12345678910", "8yd4521pu8!"]

for index, number in enumerate(phone_numbers):
    if re.search(r"\b[89]{10}", number):
        print("{} номер: всё в порядке".format(index + 1))
    else:
        print("{} номер: не подходит".format(index + 1))

# зачет!
