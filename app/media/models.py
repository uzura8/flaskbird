import enum
import base64
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
    is_delete = db.Column(db.Boolean, nullable=False, default=False)

    def soft_delete(self):
        self.is_delete = True

    def check_deleted(self):
        return self.is_delete

@db.event.listens_for(File, 'after_update')
def receive_after_update(mapper, connection, target):
    if not target.check_deleted():
        return
    from app.common.site.media import delete_media_file_caches, \
                                        media_group_by_mimetype
    media_group = media_group_by_mimetype(target.type)
    if media_group != 'photo':
        return
    delete_media_file_caches(media_group, target.name)

class FileBin(db.Model):
    __tablename__ = 'file_bin'

    name = db.Column(db.String(64), primary_key=True)
    bin = db.Column(db.LargeBinary(length=(2**32)-1))

    def get_bin(self):
        return base64.b64decode(self.bin)
