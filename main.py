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
            return 'Ошибка'

    def student_grade_sum(self, student):
        grade_sum = 0
        grade_len = 0
        if isinstance(student, Student):
            for number in self.grades:
                grade_sum = sum(self.grades[number])
            for count in self.grades.values():
                grade_len = len(count)
            self.grade_stud_average = round(grade_sum / grade_len, 1)
            return

    def __str__(self):
        super().__str__()
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.grade_stud_average} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res


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

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.grade_lect_average = []

    def lector_grade_sum(self, lecturer):
        grade_sum = 0
        grade_len = 0
        if isinstance(lecturer, Lecturer):
            for number in self.grades:
                grade_sum = sum(self.grades[number])
            for count in self.grades.values():
                grade_len = len(count)
            self.grade_lect_average = round(grade_sum / grade_len, 1)
            return

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредний балл: {self.grade_lect_average}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


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

some_lecturer.lector_grade_sum(some_lecturer)
best_student.student_grade_sum(best_student)

print(some_lecturer)
print('')
print(best_student)