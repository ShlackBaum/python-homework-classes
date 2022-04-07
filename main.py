class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg(self, student):
        self.avg_grades = 0
        self.sum_grades = 0
        self.grades_amount = 0
        self.avg_grades_course = {}

        for course, grades in self.grades.items():
            for grade in grades:
                self.sum_grades += grade
                self.grades_amount += 1
            self.avg_grades = self.sum_grades / self.grades_amount
            self.avg_grades_course[course] = self.avg_grades

    def avg_all(self, course, students=[]):
        print(f"Анализируемый курс - {course}")
        grades_sum = 0
        grades_amount = 0
        for student in students:
            print(student.name)
            for grade in student.grades.get(course):
                print(f"Суммируемая оценка - {grade}")
                grades_sum += grade
                grades_amount += 1
                print(grades_sum)
                print(grades_amount)
            avg_grades_course = grades_sum/grades_amount
        print(f"Средняя оценка всех студентов на курсе {course} равна {avg_grades_course}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grades < other.avg_grades

    def __str__(self):
        text = f"""Статус: Студент
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_grades}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {"".join(self.finished_courses)}
---"""
        return text

    def rate_lect(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        text = f"{self.name, self.surname}"
        return text

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.grades_avg = int

    def avg(self, lector):
        self.avg_grades = 0
        self.sum_grades = 0
        self.grades_amount = 0
        for grades in self.grades.values():
            for grade in grades:
                self.sum_grades += grade
                self.grades_amount += 1
        self.avg_grades = self.sum_grades / self.grades_amount

    def avg_all(self, course, lectors=[]):
        print(f"Анализируемый курс - {course}")
        grades_sum = 0
        grades_amount = 0
        for lector in lectors:
            for grade in lector.grades.get(course):
                print(f"Суммируемая оценка - {grade}")
                grades_sum += grade
                grades_amount += 1
                print(grades_sum)
                print(grades_amount)
            avg_grades_course = grades_sum/grades_amount
        print(f"Средняя оценка всех лекторов на курсе {course} равна {avg_grades_course}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.avg_grades < other.avg_grades

    def __str__(self):
        text = f"""Статус: Лектор
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_grades}
---"""
        return text

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"""Статус: Ревьюер
Имя: {self.name} 
Фамилия: {self.surname}
---"""
        return text

best_student = Student('Павел', 'Прахов', 'M')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Front-End']

worst_student = Student('Олег', 'Пипкин', 'M')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Front-End']

best_lector = Lecturer("Лектор", "Лекторович")
best_lector.courses_attached += ["Python"]
best_lector.courses_attached += ["Front-End"]

worst_lector = Lecturer("Коллектор", "Коллекторович")
worst_lector.courses_attached += ["Python"]
worst_lector.courses_attached += ["Front-End"]

cool_student = Student("Валерия", "Новодворская", "Ж")
cool_student.courses_in_progress += ["Python"]
cool_student.courses_in_progress += ["Front-End"]


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Front-End']

best_mentor = Mentor('Any', 'Buddy')
best_mentor.courses_attached += ['Python']
best_mentor.courses_attached += ['Front-End']

cool_reviewer = Reviewer("Вася", "Пупкин")
cool_reviewer.courses_attached += ["Python"]
cool_reviewer.courses_attached += ["Front-End"]

best_reviewer = Reviewer("Тимур", "Галямов")
best_reviewer.courses_attached += ["Python"]
best_reviewer.courses_attached += ["Front-End"]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Front-End', 5)
cool_reviewer.rate_hw(best_student, 'Front-End', 8)

cool_reviewer.rate_hw(worst_student, 'Python', 10)
cool_reviewer.rate_hw(worst_student, 'Python', 10)
cool_reviewer.rate_hw(worst_student, 'Front-End', 7)
cool_reviewer.rate_hw(worst_student, 'Front-End', 6)

cool_student.rate_lect(best_lector, 'Python', 10)
cool_student.rate_lect(best_lector, 'Python', 9)
cool_student.rate_lect(best_lector, 'Front-End', 10)
cool_student.rate_lect(best_lector, 'Front-End', 9)

cool_student.rate_lect(worst_lector, 'Python', 1)
cool_student.rate_lect(worst_lector, 'Python', 2)
cool_student.rate_lect(worst_lector, 'Front-End', 2)
cool_student.rate_lect(worst_lector, 'Front-End', 1)

best_lector.avg(best_lector)
best_student.avg(best_student)
worst_lector.avg(worst_lector)
worst_student.avg(worst_lector)

print(f"Лучшие оценки лектора - это {best_lector.grades} и они у лектора {best_lector}")
print(f"Лучшие оценки студента - это {best_student.grades} и они у студента {best_student}")
print(cool_reviewer)
print(best_lector)
print(worst_lector)
print(best_student)
print(worst_student)

print(best_student > worst_student)
print(best_lector > worst_lector)

best_student.avg_all("Front-End", [worst_student, best_student])
best_lector.avg_all("Front-End", [best_lector, worst_lector])

