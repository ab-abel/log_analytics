from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    lastname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, firstname, lastname, email, password):
       self.firstname = firstname
       self.lastname = lastname
       self.email = email
       self.password = password
   
    @property
    def is_authenticated(self):
        return True
   
    @property
    def is_active(self):
        return True
   
    @property
    def is_anonymous(self):
        return False
   
    def get_id(self):
        return str(self.id)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=120)])
    submit = SubmitField('Login')