from library import db
from library.models import StudentLogin, TeacherLogin, Books
db.create_all()

student = StudentLogin(username='mati', email_address='mati@mati.mati', password='123456789')
teacher = TeacherLogin(username='mati', email_address='mati@mati.mati', password='123456789')
book = Books(title='test', authors='test', language='en', categories='test', avg_rate=5)
db.session.add(student)
db.session.add(teacher)
db.session.add(book)
db.session.commit()
