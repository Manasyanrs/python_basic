questions = int(input("Кол-во видеокарт: "))

old_vga = []
new_vga = []

for number in range(1, questions + 1):
    model_vga = int(input(str(number) + " Видеокарта: "))
    old_vga.append(model_vga)


for vga in old_vga:
    if vga <= 3070:
        new_vga.append(vga)

print("\nСтарый список видеокарт:", old_vga)
print("Новый список видеокарт:", new_vga)

# зачет!
