from . import db
from datetime import datetime

class Base(db.Model):
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

class SAMember(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    sex = db.Column(db.String(1))

    @classmethod
    def change_sex(self, sex=None):
        self.sex = sex

