from classic_classes.school_classes import School, Teacher, Student

class TestSchool:
    def test_school(self):
        school = School("Pichelmayergasse")
        assert isinstance(school, School)
        assert school.name == "Pichelmayergasse"
        assert len(school.students) == 0

        assert str(school) == "Pichelmayergasse Teachers: 0 Students: 0"

    def test_add_teacher(self):
        school = School("Pichelmayergasse")
        teacher = Teacher(first_name="Rainer", last_name="Amler", birth_date="04.02.1999", personal_id=1)
        school.add_teacher(teacher=teacher)

        assert len(school.teachers) == 1

    def test_add_student(self):
        school = School("Pichelmayergasse")
        student = Student(first_name="Rainer", last_name="Amler", birth_date="04.02.1999", student_id=1)
        school.add_student(student=student)

        assert len(school.students) == 1

    def test_show_all_students(self):
        school = School("Pichelmayergasse")
        student = Student(first_name="Rainer", last_name="Amler", birth_date="04.02.1999", student_id=1)
        school.add_student(student=student)

        assert school.show_all_students() == "Rainer Amler ID: 1"

    def test_show_all_teachers(self):
        school = School("Pichelmayergasse")
        teacher = Teacher(first_name="Rainer", last_name="Amler", birth_date="04.02.1999", personal_id=1)
        school.add_teacher(teacher=teacher)

        assert school.show_all_teachers() == "Rainer Amler Personal_ID: 1"
