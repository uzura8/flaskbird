from flask import Blueprint

bp = Blueprint('site', __name__)

from . import routes
