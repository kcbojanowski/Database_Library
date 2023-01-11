import datetime
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from library import app
from library.forms import LoginForm,  RegisterForm
from library.models import StudentLogin, Students, Issue, Books
from library import db
import requests


@app.route('/')
@app.route('/home')
def home_page():
    query0 = 'SELECT * FROM books ORDER BY title'
    all_books = db.session.execute(query0)
    books_list = []
    for row in all_books:
        if row.number_of_copies != 0:
            books_dict = {'id': row.id, 'title': row.title, 'authors': row.authors, 'categories': row.categories, 'avg_rate': row.avg_rate}
            books_list.append(books_dict)

    return render_template('index.html', books=books_list)


@app.route('/', methods=['POST'])
@app.route('/home', methods=['POST'])
def home_page_post():
    data = request.get_json(force=True)
    if data:
        try:
            obj = Issue(book_id=data['id'], student_id=current_user.id)
            db.session.add(obj)
            query1 = 'UPDATE books SET number_of_copies = number_of_copies - 1 WHERE id = :book_id'
            result = db.session.execute(query1, {'book_id': data['id']})
            db.session.commit()
            return '', 204
        except:
            flash("Issue canceled", category='danger')
            return 'Issue canceled', 400
    else:
        return 'Issue canceled', 400


@app.route('/admin')
def admin_page():
    return render_template('admin.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
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


@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_info = Students(index=form.index.data, department=form.department.data, semester=form.semester.data)
        user_to_create = StudentLogin(username=form.username.data, email_address=form.email_address.data,
                                      password=form.password1.data, student_id=form.index.data)
        db.session.add(user_info)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
    return render_template('signin.html', form=form)


@app.route('/history')
def history_page():
    query0 = 'select i.id, b.title, b.authors, i.issue_date, i.return_date from books b, issue i where b.id=i.book_id order by issue_date'
    all_issues = db.session.execute(query0)
    issues_list = []
    for row in all_issues:
        issues_dict = {'id': row.id, 'title': row.title, 'authors': row.authors, 'issue_date': row.issue_date, 'return_date': row.return_date}
        issues_list.append(issues_dict)
    return render_template('history.html', issues=issues_list)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

