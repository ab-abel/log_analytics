from flask import Flask
import os

# dotenv loader
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)