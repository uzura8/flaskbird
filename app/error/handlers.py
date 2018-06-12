from flask import render_template
from app import db
from . import bp

@bp.app_errorhandler(400)
def bad_request_error(error):
    #if wants_json_response():
    #    return api_error_response(404)
    return render_template('error/400.html'), 400

@bp.app_errorhandler(404)
def not_found_error(error):
    #if wants_json_response():
    #    return api_error_response(404)
    return render_template('error/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    #if wants_json_response():
    #    return api_error_response(500)
    return render_template('error/500.html'), 500
