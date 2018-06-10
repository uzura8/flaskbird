from datetime import datetime
from flask import Blueprint, g
from flask_login import current_user
from app import db
from app.common.helper import url_static, url_media
from app.member.forms import LoginForm

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.context_processor
def helper_processor():
    return dict(url_static=url_static, url_media=url_media)

def site_auth_check(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        if current_user.is_authenticated:
            current_user.last_access = datetime.now()
            db.session.commit()
        else:
            g.login_form = LoginForm()
    return wrapper

from .models import Member
from . import routes
