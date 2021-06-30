numbers_containers = int(input("Кол-во контейнеров: "))
line_containers = []

for number in range(numbers_containers):
    questions = int(input("Введите вес контейнера: "))
    if questions > 200:
        print("Контейне привишает весь 200 кг")
    else:
        line_containers.append(questions)

new_container = int(input("\nВведите вес нового контейнера: "))

place_containers = 1

for kg in range(len(line_containers)):
    if line_containers[kg] >= new_container:
        place_containers += 1

print("\nНомер, куда встанет новый контейнер:", place_containers)