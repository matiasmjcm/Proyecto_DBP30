from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db_password = 'yourpassword'  # replace here your password

# APP CONFIGURATION
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{db_password}@localhost:5432/project_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.env = "development"

db = SQLAlchemy(app)