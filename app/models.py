from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid
# Adding in Flask Security for passwords
from werkzeug.security import generate_password_hash, check_password_hash
# creates a hex token for eventual API access
import secrets

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    open_to_work = db.Column(db.Boolean, nullable = False)
    cohort = db.Column(db.String(150))
    grad_date = db.Column(db.DateTime)
    company_id = db.Column(db.String, db.ForeignKey('company.id'))

    def __init__(self, password, first_name, last_name, email, open_to_work, cohort = '', grad_date = None, company_id = None):
        self.id = self.set_id()
        self.password = self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.open_to_work = open_to_work
        self.cohort = cohort
        self.grad_date = grad_date
        self.company_id = company_id
    
    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)
    
    def __repr__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'


class Company(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    field = db.Column(db.String(150), nullable = False)
    employees = db.relationship('User', backref='employer')
    jobs = db.relationship('Job', backref = 'company')

    def __init__(self, name, field):
        self.id = self.set_id()
        self.name = name
        self.field = field

    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return f'{self.name}'

class Job(db.Model):
    id = db.Column(db.String, primary_key = True)
    company_id = db.Column(db.String, db.ForeignKey('company.id'), nullable = False)
    title = db.Column(db.String(150), nullable = False)
    level = db.Column(db.String(150))
    salary = db.Column(db.Integer)

    def __init__(self, company_id, title, level = '', salary = 0):
        self.id = self.set_id()
        self.company_id = company_id
        self.title = title
        self.level = level
        self.salary = salary

    def set_id(self):
        return str(uuid.uuid4())