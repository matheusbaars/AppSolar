from appsolar import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=100))
    email = db.Column(db.String(length=100), unique=True, nullable=False)
    phone = db.Column(db.String(length=12))
    adress = db.Column(db.String())

    def __init__(self, name,surname, email, phone, adress):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.adress = adress

    def __repr__(self):
        return f'Name {self.name}'

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_adress = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)



