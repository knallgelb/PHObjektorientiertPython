from .student import Student
from .teacher import Teacher


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = set()
        self.students = set()

    def __str__(self):
        return f"{self.name} Teachers: {len(self.teachers)} Students: {len(self.students)}"

    def add_teacher(self, teacher: Teacher) -> Teacher:
        self.teachers.add(teacher)
        return teacher

    def add_student(self, student: Student) -> Student:
        self.students.add(student)
        return student

    def show_all_students(self):
        return "\n".join(str(x) for x in self.students)

    def show_all_teachers(self):
        return "\n".join(str(x) for x in self.teachers)
