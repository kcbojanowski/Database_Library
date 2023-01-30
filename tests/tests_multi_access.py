import unittest
from library import db
from datetime import datetime
from sqlalchemy import create_engine
from library.models import Students, Books, Issue
from sqlalchemy.orm import sessionmaker


class TestStudentsModel(unittest.TestCase):
    """
    Test case for the Students model.
    """
    def setUp(self):
        """
        Set up test data for the test cases.
        """
        # create a book
        self.book = Books(title='Book1', number_of_copies=1, language='en')
        # create two students
        self.student1 = Students(id_number=111111, department='wz', semester=1)
        self.student2 = Students(id_number=222222, department='wo', semester=2)
        # add the book and students to the database
        db.session.add_all([self.book, self.student1, self.student2])
        # commit changes to the database
        db.session.commit()

    def test_create_student(self):
        """
        Test that the student can be added to the database.
        """
        # check if the student has been added to the database
        self.assertTrue(Students.query.filter_by(id_number=111111).first())

    def test_student_attributes(self):
        """
        Test that the student has the correct attributes.
        """
        # get the student from the database
        student = Students.query.filter_by(id_number=111111).first()
        # check if the student has the correct attributes
        self.assertEqual(student.id_number, 111111)
        self.assertEqual(student.department, 'wz')
        self.assertEqual(student.semester, 1)

    def test_multi_access(self):
        """
        Test that multi-access to the database works correctly.
        """
        # create two issues with the same book
        issue1 = Issue(book_id=self.book.id, student_id=self.student1.id_number)
        issue2 = Issue(book_id=self.book.id, student_id=self.student2.id_number)
        # decrement the number of copies for the book
        query1 = f'UPDATE books SET number_of_copies = number_of_copies - 1 WHERE id = {self.book.id}'
        db.session.execute(query1)
        # add the first issue to the database
        db.session.add(issue1)
        db.session.commit()
        try:
            # try to decrement the number of copies for the book again
            db.session.execute(query1)
            # add the second issue to the database
            db.session.add(issue2)
            db.session.commit()
        except:
            # catch any errors that occur
            pass
        # get the book from the database
        book = db.session.query(Books).filter_by(title='Book1').first()
        # check if the number of copies has been updated correctly
        self.assertEqual(book.number_of_copies, 0)

    def tearDown(self):
        # remove the book from the database
        db.session.delete(self.book)
        # remove the students from the database
        db.session.delete(self.student1)
        db.session.delete(self.student2)
        db.session.commit()
        db.session.close()


if __name__ == '__main__':
    unittest.main()
