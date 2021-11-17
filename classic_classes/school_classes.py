from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    """Represent a person"""
    def __init__(self, first_name: str, last_name: str, birth_date: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")

    @abstractmethod
    def get_full_name(self):
        pass

    def __str__(self):
        return self.get_full_name()

class Student(Person):
    """Represent a student"""
    def __init__(self, first_name: str, last_name: str, birth_date: datetime, student_id: int):
        super(Student, self).__init__(first_name, last_name, birth_date)
        self.student_id = student_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} ID: {self.student_id}"

class Teacher(Person):
    """Represent a teacher"""
    def __init__(self, first_name: str, last_name: str, birth_date: datetime, personal_id: int):
        super(Teacher, self).__init__(first_name, last_name, birth_date)
        self.personal_id = personal_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} Personal_ID: {self.personal_id}"

class School:
    """Represent a school"""
    def __init__(self, name):
        self.name = name
        self.teachers = set()
        self.students = set()

    def __str__(self):
        return f"{self.name} Teachers: {len(self.teachers)} Students: {len(self.students)}"

    def add_teacher(self, teacher: Teacher) -> Teacher:
        """adds a teacher to this school"""
        self.teachers.add(teacher)
        return teacher

    def add_student(self, student: Student) -> Student:
        """adds a student to this school"""
        self.students.add(student)
        return student

    def show_all_students(self):
        """shows all students"""
        return "\n".join(str(x) for x in self.students)

    def show_all_teachers(self):
        """shows all teachers"""
        return "\n".join(str(x) for x in self.teachers)
