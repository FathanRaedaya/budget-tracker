from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create flask class called app
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from routes import *
