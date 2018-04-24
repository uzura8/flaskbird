from flask import Blueprint
from app.common.helper import url_static

bp = Blueprint('site', __name__)

@bp.context_processor
def helper_processor():
    return dict(url_static=url_static)

from . import routes
