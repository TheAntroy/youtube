from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'thisismysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo-mysql-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes
