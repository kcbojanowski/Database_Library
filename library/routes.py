import datetime
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from library import app
from library.forms import LoginForm, RegisterFormTeacherLogin, RegisterFormStudent
from library.models import TeacherLogin, StudentLogin
from library import db
import requests



@app.route('/')
@app.route('/home')
def home_page():
    query0 = 'SELECT title, authors, categories, avg_rate, number_of_copies FROM books ORDER BY title'
    all_books = db.session.execute(query0)
    books_list = []
    for row in all_books:
        if row.number_of_copies != 0:
            books_dict = {'title': row.title, 'authors': row.authors, 'categories': row.categories, 'avg_rate': row.avg_rate}
            books_list.append(books_dict)
    return render_template('index.html', books=books_list)


@app.route('/admin')
def admin_page():
    return render_template('admin.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.teacher:
            attempted_user = TeacherLogin.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(
                    attempted_password=form.password.data
            ):
                login_user(attempted_user)
                flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
                return redirect(url_for('home_page'))
            else:
                flash('Username and password are not match! Please try again', category='danger')
        else:
            attempted_user = StudentLogin.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(
                    attempted_password=form.password.data
            ):
                login_user(attempted_user)
                flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
                return redirect(url_for('home_page'))
            else:
                flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/signin')
def signin_page():
    return render_template('signin.html')


@app.route('/history')
def history_page():
    return render_template('history.html')
