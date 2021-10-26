from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/appsolar'
app.config['SECRET_KEY'] = '7d185291c0d1f4fa46f511e9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager = LoginManager(app)
login_manager.login_view = "landing_page"
login_manager.login_message_category = 'info'
from appsolar import routes