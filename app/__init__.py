from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

# Assign db to SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)

# Name and create database to save
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget_tracker.db'
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Initialise db with flask
db.init_app(app)

from . import routes
