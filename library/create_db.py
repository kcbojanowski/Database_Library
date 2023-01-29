from library import db
from library.models import StudentLogin, Books, Students
db.create_all()

student = StudentLogin(username='smati', email_address='mati@mati.mati', password='123456789', student_id=1)
studentt = Students(id_number=123456, department='wiet', semester=6)
# book = Books(title='test', authors='test', language='en', categories='test', avg_rate=5)
db.session.add(studentt)
db.session.add(student)
# db.session.add(book)
db.session.commit()
