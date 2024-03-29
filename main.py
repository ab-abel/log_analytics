from flask import Flask, render_template, session,request, flash, redirect, url_for
import os

from app.model import LoginForm, RegisterForm, User, db
from werkzeug.security import generate_password_hash, check_password_hash

# login 
from flask_login import current_user, login_user, login_required, logout_user, LoginManager

# dotenv loader
from dotenv import load_dotenv
load_dotenv()


app = Flask(os.getenv('APP_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.
        :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)

# @app.route('/')
# def hologinme():
#     return render_template('auth/login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated or not current_user.is_anonymous:
        flash('You are already logged in', 'info')
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_exist = User.query.filter_by(email=email).first()
        if not (user_exist and check_password_hash(pwhash=user_exist.password, password=password)):
            flash('Invalid email or password. Please try again.', 'danger')
            return render_template('auth/login.html', form=form)

        db.session.add(user_exist) 
        db.session.commit()
        login_user(user_exist, remember=True)
        flash('Login successfull', 'success')
        return redirect(url_for('dashboard'))

    return render_template('auth/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated or not current_user.is_anonymous:
        flash('You are already logged in', 'info')
        return redirect(url_for('dashboard'))

    form = RegisterForm()
    if form.validate_on_submit():
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = generate_password_hash(request.form.get('password'))
        email = request.form.get('email')
        
        existing_email = User.query.filter(
            User.email.like('%' + email + '%')).first()
        if existing_email:
            flash (
                'this user email is already registered', 'warning'
            )
            return render_template('auth/register.html', form=form)
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
    # print(current_user.firstname)
    return render_template('dashboard.html',user=current_user)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # db.drop_all()
    app.run(debug=True)
