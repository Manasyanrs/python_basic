class Student:
    # TODO метод студент должен быть реализован так чтобы он отвечал только за одного студента все остальное
    # TODO реализовываем вне метода
    # TODO должны быть методы получить содний балл
    # TODO вывести информацию о себе
    # TODO без списков в параметрах
    students = ["Ардаков Игорь 1 2 3 3 4 5", "Донченко Иван 4 3 3 3 5 2",
                "Бирюков Евгений 1 3 4 4 5 5", "Васильев Валерий 3 2 2 2 2 3",
                "Девин Игорь 5 3 3 3 3 4", "Угаров Виктор 3 4 4 4 5 4",
                "Зюлькин Григорий 1 5 5 5 5 5", "Гришина Ольга 2 4 3 4 3 3",
                "Карсева Полина 5 3 2 3 4 4", "Логинов Сергей 2 5 5 5 4 4 "]
    scores = []
    new_students = []

    def __init__(self):
        self.name = 0
        self.group_number = 0
        self.academic_performance = []

    def average_score(self):
        result = 0
        for element in self.students:
            element = element.split()
            self.name = element[0] + " " + element[1]
            self.group_number = element[2]
            self .academic_performance = element[3:]

            for digit in self.academic_performance:
                result += int(digit)
            self.scores.append(str(result / 5))
            self.new_students.append("{} {} {} ".format(self.name, self.group_number, result / 5))
            result = 0

    def info(self):
        print("Результаты студентов по возрастанию среднего балла.")
        print("{:20} | {:10} | {:5}\n{:35}".format("ФИ", "Н. группы", "Успеваемость", 50 * "_"))
        for digit in sorted(self.scores):
            for average_score in self.new_students:
                index = average_score.split()
                if digit == (index[-1]):
                    print("{:20} | {:10} | {:5}".format(index[0] + " " + index[1], index[2], index[3]))


student = Student()
student.average_score()
student.info()
