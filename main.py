class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_stud_average = []

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return ('Ошибка')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.grade_lect_average = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ['Python']

strict_reviewer = Reviewer("Robert", "Bolson")
strict_reviewer.courses_attached += ['Python']
strict_reviewer.courses_attached += ['Введение в программирование']

best_student.lecturer_grade(some_lecturer, 'Python', 10)
best_student.lecturer_grade(some_lecturer, 'Python', 8)
best_student.lecturer_grade(some_lecturer, 'Python', 9)

strict_reviewer.rate_hw(best_student, 'Python', 10)
strict_reviewer.rate_hw(best_student, 'Python', 7)
strict_reviewer.rate_hw(best_student, 'Python', 9)

print(some_lecturer.grades)