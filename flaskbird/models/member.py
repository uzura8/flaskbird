from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from time import time
from hashlib import md5
import jwt
from flask_login import UserMixin
from flask import current_app
from .base import Base
from flaskbird import db, login

class Member(UserMixin, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    self_introduction = db.Column(db.String(512))
    last_login = db.Column(db.DateTime, default=datetime.now())
    last_access = db.Column(db.DateTime, default=datetime.now())

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return Member.query.get(id)

@login.user_loader
def load_member(id):
    return Member.query.get(int(id))
