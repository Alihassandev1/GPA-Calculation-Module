from flask_login import login_user, login_required, logout_user
from flask import request, render_template, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from models import Student, db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def post_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = Student.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('dashboard'))
        else:
            pw_msg = 'Password is wrong!'
            return render_template('login.html', pw_msg=pw_msg)
    else:
        email_msg = 'Email not registered'
        return render_template('login.html', email_msg=email_msg)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def post_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    user = Student.query.filter_by(email=email).first()
    if user:
        msg = 'this email is already register!'
        return render_template('signup.html', msg=msg)
    newUser = Student(name=name, email=email, password=generate_password_hash(password))
    db.session.add(newUser)
    db.session.commit()
    login_user(newUser)
    return redirect(url_for('dashboard'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))