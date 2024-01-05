from flask import Flask, render_template
import os

# dotenv loader
from dotenv import load_dotenv
load_dotenv()


app = Flask(os.getenv('APP_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('auth/login.html')


if __name__ == '__main__':
    app.run(debug=True)