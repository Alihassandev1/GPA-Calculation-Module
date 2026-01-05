from flask import Flask, render_template, url_for, redirect, request, session, flash
from models import db, Student, Subject, Semester
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from calculation import calculate_sgpa, gpaScale, calculate_cgpa
from auth import auth
from psycopg2 import connect
from datetime import datetime   

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres2030@localhost:5432/gpaResults" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '23erwfgbgd43124fghjrtght43rtgergwtr3r4tgf'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))

app.register_blueprint(auth)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    user_id = current_user.id
    
    if request.method == 'POST':
        subName = request.form.getlist('subName')
        credits = request.form.getlist('credits')
        marks = request.form.getlist('marks')
        
        # Convert to proper types
        credits = [int(c) for c in credits if c]
        marks = [float(m) for m in marks if m]

        totalC = sum(credits)
        
        if not credits or not marks:
            return render_template('GPA.html', error="Please enter valid data")
        
        # Calculate SGPA once (outside the loop)
        sgpa_value = calculate_sgpa(marks, credits)
        
        # Create one Semester record
        semester = Semester(sgpa=sgpa_value, std_id=user_id, t_credit=totalC)
        db.session.add(semester)
        db.session.flush()  # Get the semester ID before creating subjects
        
        # Create Subject records for each course
        for i in range(len(subName)):
            if subName[i]:  # Only add if name is provided
                subject = Subject(
                    name=subName[i], 
                    credit=credits[i], 
                    marks=marks[i],
                    sem_id=semester.id,
                    std_id=user_id
                )
                db.session.add(subject)
        
        db.session.commit()
        Sgpas = Semester.query.filter_by(std_id=user_id).all()
        sgpas = [sgpa.sgpa for sgpa in Sgpas]
        credits = [sgpa.t_credit for sgpa in Sgpas]
        cgpa = calculate_cgpa(sgpas, credits)
        current_user.cgpa = cgpa
        db.session.commit()
        return render_template('GPA.html', sgpa=round(sgpa_value, 2))

    return render_template('GPA.html')


@app.route('/dashboard')
@login_required 
def dashboard():
    semesters = Semester.query.filter_by(std_id=current_user.id).all()
    subject = Subject.query.filter_by(std_id=current_user.id).all()
    return render_template('dashboard.html', user=current_user, now=datetime.now(), semesters=semesters, subject=subject)

@app.route('/update_user', methods=['POST'])
@login_required
def update_user():
    name = request.form.get('name')
    email = request.form.get('email')
    current_user.name = name
    current_user.email = email
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ ==  "__main__":
    app.run(debug=True)

    
