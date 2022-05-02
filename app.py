from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

db_password = '1234'  # replace here your password

# APP CONFIGURATION
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{db_password}@localhost:5432/project_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.env = "development"

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class BookProduct(db.Model):
    __tablename__ = "bookproducts"
    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer)
    price = db.Column(db.Integer)
    due_date = db.Column(db.Date)
    borrowed_date = db.Column(db.Date)

    def __repr__(self):
        return f"Book: ISBN = {self.ISBN}, price ={self.price}, dueDate = {self.dueDate}," \
               f" borrowedDate = {self.borrowed_date}"


class Book(db.Model):
    __tablename__ = "books"
    ISBN = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    subject = db.Column(db.String)
    language = db.Column(db.String)
    actual_user = db.Column(db.String)
    publisher = db.Column(db.String)
    number_of_pages = db.Column(db.Integer)
    publication_date = db.Column(db.Date)

    def __repr__(self):
        return f"Book: ISBN={self.ISBN}, title = {self.title}, author ={self.author}, subject = {self.subject} \
        language = {self.language}, publisher = {self.publisher}, numberOfPages = {self.number_of_pages}," \
               f"publicationDate= {self.publication_date}"


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date)

    def __repr__(self):
        return f"Author: id = {self.id}, name = {self.name}, dob = {self.dob}"


class Person(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)

    def __repr__(self):
        return f"User: id={self.id}, first_name = {self.first_name}, last_name ={self.last_name}"


class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    number_of_sanctions = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)
    current_books = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return f"Account: id={self.id}, correo = {self.correo} username = {self.username}," \
               f" password = {self.password}, numberOfSanctions = {self.number_of_sanctions}, isActive = {self.is_active}"


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/signup", methods=['POST', "GET"])
def signup():
    error = False
    response = {}
    try:
        request_data = request.get_json()
        first_name = request_data["firstName"]
        last_name = request_data["lastName"]
        email = request_data["email"]
        username = request_data["username"]
        password = request_data["password"]
        account = Account(username=username, password=password, number_of_sanctions=0, is_active=True, current_books="",
                          email=email)
        db.session.add(account)
        db.session.commit()
    except Exception as e:
        error = True
        print(e)
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
