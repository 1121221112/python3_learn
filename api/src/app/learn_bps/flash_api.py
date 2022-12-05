# *_*coding:utf-8 *_*

from app import app
from flask import Blueprint, flash, redirect, render_template, request, url_for

flash_api = Blueprint('flash_api', __name__)

app.secret_key = 'random string'


@flash_api.route('/')
def index():
    return render_template('index.html')


@flash_api.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('flash_api.index'))

    return render_template('login.html', error=error)
