from flaskbird.database import db
from .base import Base

class Member(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.String(1))

    def __repr__(self):
        return '<Member {}>'.format(self.name)

    @classmethod
    def change_sex(self, sex=None):
        self.sex = sex

