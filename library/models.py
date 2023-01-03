from library import db, login_manager
from library import bcrypt
from flask_login import UserMixin
import datetime
from dateutil.relativedelta import relativedelta


class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    index = db.Column(db.Integer(), nullable=False)
    department = db.Column(db.String(length=60), nullable=False)
    semester = db.Column(db.Integer(), nullable=False)
    issue = db.relationship('Issue', back_populates='issue', lazy=False)
    login = db.relationship('StudentLogin', back_populates='studentlogin', lazy=False)


class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=60), nullable=False)
    department = db.Column(db.String(length=60), nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    login = db.relationship('TeacherLogin', back_populates='teacherlogin', lazy=False)


@login_manager.user_loader
def load_user_student(user_id):
    return StudentLogin.query.get(int(user_id))


class StudentLogin(db.Model, UserMixin):
    __tablename__ = 'studentlogin'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    number_of_books = db.Column(db.Integer())
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'), nullable=False)
    student = db.relationship('Students', back_populates='students', lazy=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


@login_manager.user_loader
def load_user_teacher(user_id):
    return TeacherLogin.query.get(int(user_id))


class TeacherLogin(db.Model, UserMixin):
    __tablename__ = 'teacherlogin'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    teacher_id = db.Column(db.Integer(), db.ForeignKey('teachers.id'), nullable=False)
    teacher = db.relationship('Teachers', back_populates='teachers', lazy=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=255), nullable=False)
    authors = db.Column(db.String(length=255))
    language = db.Column(db.String(length=255))
    categories = db.Column(db.String(length=255))
    avg_rate = db.Column(db.Integer())
    number_of_copies = db.Column(db.Integer())
    issue = db.relationship('Issue', back_populates='issue', lazy=False)


class Issue(db.Model):
    __tablename__ = 'issue'
    id = db.Column(db.Integer(), primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey('books.id'), nullable=False)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'), nullable=False)
    issue_date = db.Column(db.DateTime(), nullable=False, default=datetime.date.today())
    return_date = db.Column(db.DateTime(), nullable=False, default=datetime.date.today() + relativedelta(months=1))
    book = db.relationship("Books", back_populates="books", lazy=False)
    student = db.relationship("Students", back_populates="students", lazy=False)
