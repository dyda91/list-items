from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask (__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

db.init_app(app)
conexao = 'sqlite:///database.db'

migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

