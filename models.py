from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(200), nullable=False)
    cgpa = db.Column(db.Float())
    created_at = db.Column(db.DateTime, default=db.func.now())

    semesters = db.relationship('Semester', backref='Student', lazy=True)
    subjects = db.relationship('Subject', backref='Student', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'cgpa': self.cgpa,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') 
            if self.created_at else None
        }

class Semester(db.Model):   
    id = db.Column(db.Integer, primary_key = True)
    sgpa = db.Column(db.Float())
    t_credit = db.Column(db.Integer())
    std_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'sgpa': self.sgpa,
            't_credit': self.t_credit,
            'std_id': self.std_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') 
            if self.created_at else None
        }


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    credit = db.Column(db.Float())
    marks = db.Column(db.Float())
    grade = db.Column(db.String(2))
    sem_id = db.Column(db.Integer, db.ForeignKey('semester.id'))
    std_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'credit': self.credit,
            'grade': self.grade,
            'sem_id': self.sem_id,
            'std_id': self.std_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') 
            if self.created_at else None
        }

# class CGPA(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     cgpa = db.Column(db.Float())
#     std_id = db.Column(db.Integer, db.ForeignKey('student.id'))
#     created_at = db.Column(db.DateTime, default=db.func.now())
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'cgpa': self.cgpa,
#             'std_id': self.std_id,
#             'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') 
#             if self.created_at else None
#         }