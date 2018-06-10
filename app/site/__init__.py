from flask import Blueprint, g
from flask_babel import get_locale
from app.common.helper import url_static, url_media

bp = Blueprint('site', __name__)

@bp.context_processor
def helper_processor():
    return dict(url_static=url_static, url_media=url_media)

def site_before_request(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        g.locale = str(get_locale())
    return wrapper

from . import routes

