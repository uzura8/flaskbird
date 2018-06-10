from flask import Blueprint

bp = Blueprint('media', __name__, url_prefix='/media')

from .models import File, FileBin
#from . import routes
