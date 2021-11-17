from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name: str, last_name: str, birth_date: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")

    @abstractmethod
    def get_full_name(self):
        pass