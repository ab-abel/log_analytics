from flask import Flask, render_template, session,request, flash, redirect, url_for
import os

from app.model import LoginForm, RegisterForm, User, db

# dotenv loader
from dotenv import load_dotenv
load_dotenv()


app = Flask(os.getenv('APP_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('auth/login.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('username'):
        flash('You are already logged in', 'info')
        return redirect(url_for('login'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password') 
        email = request.form.get('email')
        existing_email = User.query.filter(
            User.email.like('%' + email + '%')).first()
        if existing_email:
            flash (
                'this user email is already registered', 'warning'
            )
        user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password
            )
        db.session.add(user)
        db.session.commit()
        flash('You are now register. Please login', 'succcess')
        
        return redirect(url_for('login'))
    if form.errors:
        flash(form.error, 'danger')
    return render_template('auth/register.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
