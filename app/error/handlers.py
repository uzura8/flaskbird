from flask import render_template
from app import db
from app.error import bp

@bp.errorhandler(400)
@bp.errorhandler(404)
@bp.errorhandler(500)
def error_handler(error):
    if error == 500:
        db.session.rollback()
    return render_template('error/{}.html'.format(error)), error
    
