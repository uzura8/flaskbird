from flask import Blueprint
from app.common.helper import url_static

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.context_processor
def helper_processor():
    return dict(url_static=url_static)

from .models import Member
from . import routes
