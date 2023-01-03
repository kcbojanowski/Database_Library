import datetime
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from library import app
from library import db
import requests


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/admin')
def home_page():
    return render_template('admin.html')


@app.route('/login')
def home_page():
    return render_template('login.html')


@app.route('/signin')
def home_page():
    return render_template('signin.html')


@app.route('/history')
def home_page():
    return render_template('history.html')
