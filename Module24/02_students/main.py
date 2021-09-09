class Student:

    def __init__(self, surname, name, group_number, academic_performance):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance

    def average_score(self):
        student_grades = 0
        for grades in self.academic_performance:
            student_grades += int(grades)
        return str(student_grades/len(self.academic_performance))

    def info(self):
        return "{} {} {} {}".format(self.surname, self.name, self.group_number, self.average_score())


students = ["Ардаков Игорь 1 2 3 3 4 5", "Донченко Иван 4 3 3 3 5 2",
            "Бирюков Евгений 1 3 4 4 5 5", "Васильев Валерий 3 2 2 2 2 3",
            "Девин Игорь 5 3 3 3 3 4", "Угаров Виктор 3 4 4 4 5 4",
            "Зюлькин Григорий 1 5 5 5 5 5", "Гришина Ольга 2 4 3 4 3 3",
            "Карсева Полина 5 3 2 3 4 4", "Логинов Сергей 2 5 5 5 4 4 "]

scores = []
new_students = []
for student in students:
    student = student.split()
    person = Student(student[0], student[1], student[2], student[3:])
    if person.average_score() not in scores:
        scores.append(person.average_score())
    new_students.append(person.info())

print("Результаты студентов по возрастанию среднего балла.")
print("{:20} | {:10} | {:5}\n{:35}".format("ФИ", "Н. группы", "Успеваемость", 50 * "_"))
for digit in sorted(scores):
    for average_score in new_students:
        index = average_score.split()
        if digit == index[-1]:
            print("{:20} | {:10} | {:5}".format(index[0] + " " + index[1], index[2], index[3]))
