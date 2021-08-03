def pedigree(name):
    if name not in persons:
        results[name] = 0
        return 0
    parent = persons[name]
    if parent in results:
        generation = results[parent] + 1
    else:
        generation = pedigree(parent) + 1
    results[name] = generation
    return generation


number_persons = int(input("Введите количество человек: "))
persons = dict()

for number in range(1, number_persons):
    input_persons = input("{} пара: ".format(number)).split()
    persons[input_persons[0]] = input_persons[1]

persons_names = set(persons.keys() | persons.values())
results = dict()

for p_name in persons_names:
    if p_name not in results:
        pedigree(p_name)

print("\n“Высота” каждого члена семьи:")
for element in sorted(results):
    print(element, results[element])

# зачет!
