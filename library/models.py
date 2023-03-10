from sqlalchemy import CheckConstraint
from sqlalchemy.orm import validates
from library import db, login_manager
from library import bcrypt
from flask_login import UserMixin
import datetime
from dateutil.relativedelta import relativedelta


class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    id_number = db.Column(db.Integer(), CheckConstraint("id_number >= 111111 AND id_number <= 999999"), nullable=False,
                          unique=True)
    department = db.Column(db.String(length=6), CheckConstraint("length(department) <=6"), nullable=False)
    semester = db.Column(db.Integer(), CheckConstraint("semester >= 1 AND semester <= 9"), nullable=False)
    issues = db.relationship('Issue', cascade="all,delete", back_populates='student', lazy=False)
    login = db.relationship('StudentLogin', cascade="all,delete", back_populates='student', lazy=False)


@login_manager.user_loader
def load_user(user_id):
    return StudentLogin.query.get(int(user_id))


class StudentLogin(db.Model, UserMixin):
    __tablename__ = 'studentlogin'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), CheckConstraint("length(username) <= 30"), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), CheckConstraint("email_address LIKE '%_@__%.__%'"), nullable=False,
                              unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id_number'), nullable=False)
    student = db.relationship('Students', back_populates='login', lazy=False)

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
    language = db.Column(db.String(length=6), CheckConstraint("length(language) <=6"))
    categories = db.Column(db.String(length=255))
    avg_rate = db.Column(db.Integer())
    number_of_copies = db.Column(db.Integer(), CheckConstraint("number_of_copies >= 0"))
    issues = db.relationship('Issue', cascade="all,delete", back_populates='book', lazy=False)


class Issue(db.Model):
    __tablename__ = 'issue'
    id = db.Column(db.Integer(), primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey('books.id'), nullable=False)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id_number'), nullable=False)
    issue_date = db.Column(db.DateTime(), nullable=False, default=datetime.date.today())
    return_date = db.Column(db.DateTime(), nullable=False, default=datetime.date.today() + relativedelta(months=1))
    book = db.relationship("Books", back_populates="issues", lazy=False)
    student = db.relationship("Students", back_populates="issues", lazy=False)
