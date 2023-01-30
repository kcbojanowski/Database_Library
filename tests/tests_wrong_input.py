import unittest
from library import db
from library.models import Students


# Test class for invalid inputs for Students model
class TestStudentsModel(unittest.TestCase):

    # Test that adding a student with an id_number of length less than 6 raises an exception
    def test_student_id_number_invalid(self):
        # Create a student object with id_number of length less than 6
        student = Students(id_number=1111, department='WGGIS', semester=1)
        # Add the student object to the session
        db.session.add(student)
        # Assert that committing the session raises an exception
        self.assertRaises(Exception, db.session.commit)

    # Test that adding a student with an invalid department raises an exception
    def test_student_department_invalid(self):
        # Create a student object with an invalid department
        student = Students(id_number=111111, department='WGGISGGG', semester=1)
        db.session.add(student)
        self.assertRaises(Exception, db.session.commit)

    # Test that adding a student with an invalid semester raises an exception
    def test_student_semester_invalid(self):
        # Create a student object with an invalid semester
        student = Students(id_number=111111, department='WGGIS', semester=10)
        db.session.add(student)
        self.assertRaises(Exception, db.session.commit)


if __name__ == '__main__':
    unittest.main()
