print("Числа Ip разделить точкой")
ipaddress = input("Введите IP: ")
new_ip = ""
for element in ipaddress:
    if element != ".":
        new_ip += element
    else:
        new_ip += " "

new_ip = new_ip.split()
count_true_iterations = 0
for digit in new_ip:
    if digit:
        if "," in digit:
            print("Адрес - это четыре числа, разделенные точками")
            break
        elif not digit.isdigit():
            print(digit + "- не целое число")
            break
        elif int(digit) > 255:
            print(digit, " превышает 255")
            break
        count_true_iterations += 1

if count_true_iterations == 4:
    print("IP-адрес корректен")
