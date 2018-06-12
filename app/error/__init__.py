from flask import Blueprint
from app.common.helper import url_static, url_media

bp = Blueprint('error', __name__, url_prefix='/error')

@bp.app_context_processor
def helper_processor():
    return dict(url_static=url_static, url_media=url_media)

from . import handlers

