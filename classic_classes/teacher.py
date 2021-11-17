from datetime import datetime

from .person import Person

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, birth_date: datetime, personal_id: int):
        super(Teacher, self).__init__(first_name, last_name, birth_date)
        self.personal_id = personal_id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} Personal_ID: {self.personal_id}"

