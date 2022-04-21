class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                if grade > 10:
                    lecturer.grades[course] = [10]
                elif grade < 1:
                    lecturer.grades[course] = [1]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    #     Добавить метод вычисления среднего балла за домашки. Убрать определение среднего из __str__
    def average(self, grades):
        self.average = sum(sum(grades.values(), [])) / len(grades)
        return self.average

    def __str__(self):
        progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average}\n' \
              f'Курсы в процессе изучения: {progress}\n' \
              f'Завершённые курсы: {finished}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = 0

    #     Оставил вычисление среднего в __str__, кажется, это проще, чем делать через метод.
    def __str__(self):
        self.average = sum(sum(self.grades.values(), [])) / len(self.grades)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average < other.average


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Mark', 'Ruffalo', 'Male')
best_student.courses_in_progress += ['Python', 'Django']
best_student.finished_courses += ['Git']
second_student = Student('Chris', 'Evans', 'Male')
second_student.courses_in_progress += ['Python', 'Django', 'C#', 'HTML']
second_student.finished_courses += ['Git', 'C++', 'SMM']
lecturer = Lecturer('Chris', 'Hemsworth')
lecturer.courses_attached += ['Python', 'Ruby', 'Git', 'Django']
lecturer_iron = Lecturer('Robert', 'Downey Jr.')
lecturer_iron.courses_attached += ['CSS', 'C#', 'Git', 'Python']
rewiewer = Reviewer('Tom', 'Hiddleston')
rewiewer.courses_attached += ['Python', 'Django']
rewiewer.rate_hw(best_student, 'Python', 10)
rewiewer.rate_hw(best_student, 'Django', 8)
rewiewer.rate_hw(second_student, 'Python', 8)
rewiewer.rate_hw(second_student, 'Django', 9)
rewiewer.rate_hw(second_student, 'C#', 10)
rewiewer.rate_hw(second_student, 'HTML', 10)
Student.average(best_student, best_student.grades)
Student.average(second_student, second_student.grades)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Django', 7)
second_student.rate_lecturer(lecturer_iron, 'Python', 10)
second_student.rate_lecturer(lecturer_iron, 'C#', 9)
print(f'Студент:\n{best_student}\n')
print(f'Студент:\n{second_student}\n')
print(f'Лектор:\n{lecturer}\n')
print(f'Лектор:\n{lecturer_iron}\n')
print(f'Проверяющий:\n{rewiewer}\n')
print(best_student > second_student)
print(lecturer < lecturer_iron)
student_list = [best_student, second_student]
lecturer_list = [lecturer, lecturer_iron]


def course_average_grade(students, course):
    grade = 0
    for student in students:
        if course in student.grades:
            grade += sum(student.grades[course])
    grade /= len(students)
    return grade


def lecturers_average_grade(lecturers, course):
    grade = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grade += sum(lecturer.grades[course])
    grade /= len(lecturers)
    return grade


print(course_average_grade(student_list, 'Django'))
print(lecturers_average_grade(lecturer_list, 'Python'))