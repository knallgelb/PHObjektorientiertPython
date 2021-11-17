from datetime import datetime

from use_dataclasses.school_classes import Student


class TestStudent:
    def test_get_full_name(self):
        student = Student(
            first_name="Max",
            last_name="Mustermann",
            birthdate="28.02.1999",
            student_id=12345)
        assert student.first_name == "Max"
        assert student.last_name == "Mustermann"
        assert student.student_id == 12345
        assert student.birthdate == datetime(year=1999, day=28, month=2)
        assert student.get_full_name() == "Max Mustermann ID: 12345 Birthday: 28.02.1999"
