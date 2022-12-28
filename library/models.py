from library import db, login_manager
from library import bcrypt
from flask_login import UserMixin
import datetime


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

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Books(db.Model, UserMixin):
    __tablename__ = 'books'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=255), nullable=False)
    authors = db.Column(db.String(length=255))
    language = db.Column(db.String(length=255))
    categories = db.Column(db.String(length=255))
    avg_rate = db.Column(db.Integer())