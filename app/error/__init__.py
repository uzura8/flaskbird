from flask import Blueprint

bp = Blueprint('error', __name__, url_prefix='/error')

from . import handlers
