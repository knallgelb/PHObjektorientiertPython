from dataclasses import dataclass, field
from datetime import datetime
from abc import ABC, abstractmethod

@dataclass
class Person(ABC):
    """Represent a person"""
    first_name: str
    last_name: str
    birthdate: datetime

    def __post_init__(self):
        self.birthdate = datetime.strptime(self.birthdate, "%d.%m.%Y")

    @abstractmethod
    def get_full_name(self):
        pass

    def __str__(self):
        return self.get_full_name()

@dataclass
class Student(Person):
    """Represent a student"""
    student_id: int

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} ID: {self.student_id} Birthday: {datetime.strftime(self.birthdate, '%d.%m.%Y') }"

@dataclass
class Teacher(Person):
    """Represent a teacher"""
    personal_id: int

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} Personal_ID: {self.personal_id}"

@dataclass
class School:
    """Represent a school"""
    name: str
    teachers: list[Teacher] = field(default_factory=list)
    students: list[Student] = field(default_factory=list)

    def __str__(self):
        return f"{self.name} Teachers: {len(self.teachers)} Students: {len(self.students)}"

    def add_teacher(self, teacher: Teacher) -> Teacher:
        """adds a teacher to this school"""
        self.teachers.append(teacher)
        return teacher

    def add_student(self, student: Student) -> Student:
        """adds a student to this school"""
        self.students.append(student)
        return student

    def show_all_students(self):
        """shows all students"""
        return "\n".join(str(x) for x in self.students)

    def show_all_teachers(self):
        """shows all teachers"""
        return "\n".join(str(x) for x in self.teachers)


p = Student(first_name="Rainer", last_name="Amler", birthdate="04.02.1980", student_id="1234")
print(p.get_full_name())