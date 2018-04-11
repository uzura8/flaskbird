from flaskbird.database import db
from datetime import datetime

class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    #def __init__(self):
    #    self.created_at = datetime.utcnow()
    #    self.updated_at = datetime.utcnow()