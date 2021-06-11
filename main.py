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
        if isinstance(student, Student):
            for number in self.grades:
                grade_sum = sum(self.grades[number])
                for count in self.grades.values():
                    grade_len = len(count)
                    if grade_sum != 0 and grade_len != 0:
                        self.grade_stud_average = round(grade_sum / grade_len, 1)
                    else:
                        return 'Ошибка'

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
        if isinstance(lecturer, Lecturer):
            for number in self.grades:
                grade_sum = sum(self.grades[number])
                for count in self.grades.values():
                    grade_len = len(count)
                    if grade_sum != 0 and grade_len != 0:
                        self.grade_lect_average = round(grade_sum / grade_len, 1)
                    else:
                        return 'Ошибка'

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

worst_student = Student('Max', 'Payne', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Forrest', 'Gump')
another_lecturer.courses_attached += ['Введение в программирование']

strict_reviewer = Reviewer("Robert", "Bolson")
strict_reviewer.courses_attached += ['Python']
strict_reviewer.courses_attached += ['Введение в программирование']

best_student.lecturer_grade(some_lecturer, 'Python', 10)
best_student.lecturer_grade(some_lecturer, 'Python', 8)
best_student.lecturer_grade(some_lecturer, 'Python', 9)

best_student.lecturer_grade(another_lecturer, 'Введение в программирование', 7)
best_student.lecturer_grade(another_lecturer, 'Введение в программирование', 8)
best_student.lecturer_grade(another_lecturer, 'Введение в программирование', 6)

worst_student.lecturer_grade(some_lecturer, 'Python', 6)
worst_student.lecturer_grade(some_lecturer, 'Python', 5)
worst_student.lecturer_grade(some_lecturer, 'Python', 5)

worst_student.lecturer_grade(another_lecturer, 'Введение в программирование', 6)
worst_student.lecturer_grade(another_lecturer, 'Введение в программирование', 4)
worst_student.lecturer_grade(another_lecturer, 'Введение в программирование', 7)

strict_reviewer.rate_hw(best_student, 'Python', 10)
strict_reviewer.rate_hw(best_student, 'Python', 7)
strict_reviewer.rate_hw(best_student, 'Python', 9)

strict_reviewer.rate_hw(worst_student, 'Введение в программирование', 3)
strict_reviewer.rate_hw(worst_student, 'Введение в программирование', 4)
strict_reviewer.rate_hw(worst_student, 'Введение в программирование', 5)

some_lecturer.lector_grade_sum(some_lecturer)
best_student.student_grade_sum(best_student)
another_lecturer.lector_grade_sum(another_lecturer)
worst_student.student_grade_sum(worst_student)

print(some_lecturer)
print()
print(another_lecturer)
print()
print(best_student)
print()
print(worst_student)

# print(worst_student.grades)
# print(another_lecturer.grades)