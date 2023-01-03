from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from library.models import StudentLogin, TeacherLogin


class RegisterFormStudent(FlaskForm):
    def validate_username_student(self, username_to_check):
        student = StudentLogin.query.filter_by(username=username_to_check.data).first()
        if student:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address_student = StudentLogin.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address_student:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(validators=[Email(), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Register")


class RegisterFormTeacherLogin(FlaskForm):
    def validate_username_teacher(self, username_to_check):
        teacher = TeacherLogin.query.filter_by(username=username_to_check.data).first()
        if teacher:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_teacher(self, email_address_to_check):
        email_address_teacher = TeacherLogin.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address_teacher:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(validators=[Email(), DataRequired()])
    password1 = PasswordField(validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Register")


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    teacher = SelectField(label="Teacher", choices=[(True, 'Teacher')])
    submit = SubmitField(label="Log in")
