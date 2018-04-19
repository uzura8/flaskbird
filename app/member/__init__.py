from flask import Blueprint

bp = Blueprint('member', __name__, url_prefix='/member')

from app.member.models import Member
from app.member import routes
