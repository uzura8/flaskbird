from flask import Blueprint

bp = Blueprint('member', __name__, url_prefix='/member')

from .models import Member
from . import routes
