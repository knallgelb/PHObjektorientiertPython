from datetime import datetime

from classic_classes.teacher import Teacher


class TestTeacher:
    def test_get_full_name(self):
        teacher = Teacher(
            first_name="Max",
            last_name="Mustermann",
            birth_date="28.02.1999",
            personal_id=12345)
        assert teacher.first_name == "Max"
        assert teacher.last_name == "Mustermann"
        assert teacher.personal_id == 12345
        assert teacher.birth_date == datetime(year=1999, day=28, month=2)
        assert teacher.get_full_name() == "Max Mustermann Personal_ID: 12345"
