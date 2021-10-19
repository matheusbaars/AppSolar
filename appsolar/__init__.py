from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/appsolar'
app.config['SECRET_KEY'] = '7d185291c0d1f4fa46f511e9'
db = SQLAlchemy(app)



from appsolar import routes