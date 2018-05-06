from flask import render_template, g
from flask_babel import _, get_locale
from app.site import bp

@bp.before_request
def before_request():
    g.locale = str(get_locale())

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/members')
@bp.route('/members/')
@bp.route('/members/<path>')
def members(path=''):
    return render_template('members.html')

