def interests_students(dictionary_type):
    students_hobby = []
    students_surname = 0
    for outside_interest in dictionary_type.values():

        students_hobby += outside_interest["interests"]
        students_surname += len(outside_interest["surname"])
    return students_hobby, students_surname


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

for id_student, age_student in students.items():
    print("Id студента = {id}, возраст = {student_age}".format(
        id=id_student,
        student_age=age_student["age"]
    ))
hobby, length_all_students_surname = interests_students(students)
print("\nИнтересы всех студентов: \n{interests} \nОбщая длину фамилий всех студентов\n{length}".format(
    interests=hobby,
    length=length_all_students_surname
))

print()

students_interests = hobby
students_surname_length = length_all_students_surname

print(students_interests)
print(students_surname_length)

# зачет!
