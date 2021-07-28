named_dishes = input("Названий блюд, разделённые символом ';' ")
print("\nДоступное меню:", named_dishes)
new_name = ""
for name in named_dishes:
    if name != ";":
        new_name += name
    else:
        new_name += ", "
print("\nНа данный момент в меню есть:", new_name)
