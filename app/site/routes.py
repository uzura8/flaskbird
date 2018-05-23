from flask import render_template
from . import bp, site_before_request
from app.member import site_auth_check

@bp.before_request
@site_before_request
@site_auth_check
def before_request():
    pass

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/members')
@bp.route('/members/')
@bp.route('/members/<path>')
def members(path=''):
    return render_template('members.html')

