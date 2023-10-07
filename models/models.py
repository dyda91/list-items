from enum import unique
from re import T
from flask_login import UserMixin
from config import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String, nullable=False)

    info = db.relationship('Itens', backref='itens', lazy=True)

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

        db.create_all()
        db.session.commit()

    def __repr__(self):
        return "<User %r>" % self.username





class Itens(db.Model):
    __tablename__='itens'
    id = db.Column(db.Integer, primary_key=True)   
    user_username = db.Column(db.Integer, db.ForeignKey('users.username'))
    situação = db.Column(db.String)
    descrição = db.Column(db.String)
    item = db.Column(db.String)
    codigo_item = db.Column(db.String)

    def __init__(self, user_username, situação, descrição, item, codigo_item):
        self.user_username = user_username
        self.situação = situação
        self.descrição = descrição
        self.item = item
        self.codigo_item = codigo_item

        db.create_all()
        db.session.commit()


    def __repr__(self):
        return 'Item: {}' .format(self.item)