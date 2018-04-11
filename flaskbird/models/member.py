from werkzeug.security import generate_password_hash, check_password_hash
from flaskbird.database import db
from .base import Base

class Member(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    sex = db.Column(db.String(1))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#    @classmethod
#    def change_sex(self, sex=None):
#        self.sex = sex

