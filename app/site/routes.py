from flask import render_template
from app.site import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/members')
@bp.route('/members/')
@bp.route('/members/<path>')
def members(path=''):
    return render_template('members.html')

