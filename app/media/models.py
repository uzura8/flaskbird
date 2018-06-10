import enum
from datetime import datetime
from app import db
from app.models.base import TimestampMixin

UserType = enum.Enum('UserType', 'member admin')

class File(TimestampMixin, db.Model):
    name = db.Column(db.String(64), primary_key=True)
    type = db.Column(db.String(64), nullable=False)
    size = db.Column(db.Integer, nullable=False, default=0)
    user_type = db.Column(db.Enum(UserType), nullable=False)
    original_name = db.Column(db.String(128), nullable=False)
    exif = db.Column(db.Text)
    shot_at = db.Column(db.DateTime, default=datetime.utcnow)

class FileBin(db.Model):
    __tablename__ = 'file_bin'

    name = db.Column(db.String(64), primary_key=True)
    bin = db.Column(db.LargeBinary(length=(2**32)-1))

