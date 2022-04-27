from configuration import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User: id={self.id}, firstName = {self.firstName}, lastName ={self.lastName}, password ={self.password}"

class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    nSanctions = db.Column(db.Integer)
    isActive = db.Column(db.String)

    def __repr__(self):
        return f"Account: id={self.id}, correo = {self.correo} username = {self.username}, password = {self.password}, nSactions = {self.nSanctions}, isActive = {self.isActive}"


class Book(db.Model):
    __tablename__ = "books"
    ISBN = db.Column(db.Integer, primary_key=True) #Books code
    title = db.Column(db.String)
    author = db.Column(db.String, db.ForeignKey("Author.name"))
    subject = db.Column(db.String)
    language = db.Column(db.String)
    publisher = db.Column(db.String)
    numberOfPages = db.Column(db.String)
    publicationDate = db.Column(db.Date)

    def __repr__(self):
        return f"Book: ISBN={self.ISBN}, title = {self.title}, author ={self.author}, subject = {self.subject} \
        language = {self.language}, publisher = {self.publisher}, numberOfPages = {self.numberOfPages}, publicationDate= {self.publicationDate}"


class BookProduct(db.Model):
    __tablename__ = "bookproducts"
    id = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer, db.ForeignKey("Book.ISBN"))
    price = db.Column(db.Integer)
    dueDate = db.Column(db.Date)
    borrowedDate = db.Column(db.Date)

    def __repr__(self):
        return f"Book: ISBN = {self.ISBN}, price ={self.price}, dueDate = {self.dueDate}, borrowedDate = {self.borrowedDate}"


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date)

    def __repr__(self):
        return f"Author: id = {self.id}, name = {self.name}, dob = {self.dob}"
