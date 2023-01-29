import unittest
from library import db
from library.models import Students


class TestStudentsModel(unittest.TestCase):

    def setUp(self):
        self.student = Students(index=111111, department='WIET', semester=3)
        db.session.add(self.student)
        db.session.commit()

    def test_create_student(self):
        # Test that the student is added to the database
        self.assertTrue(Students.query.filter_by(index=111111).first())

    def test_student_attributes(self):
        # Test that the student has the correct attributes
        student = Students.query.filter_by(index=111111).first()
        self.assertEqual(student.id_number, 111111)
        self.assertEqual(student.department, 'WIET')
        self.assertEqual(student.semester, 3)

    def tearDown(self):
        # Clean up the database after the test
        Students.query.filter_by(index=111111).delete()
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
