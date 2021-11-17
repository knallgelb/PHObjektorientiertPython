from datetime import datetime

from .person import Person

class Student(Person):
    def __init__(self, first_name: str, last_name: str, birth_date: datetime, student_id: int):
        super(Student, self).__init__(first_name, last_name, birth_date)
        self.student_id = student_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} ID: {self.student_id}"


