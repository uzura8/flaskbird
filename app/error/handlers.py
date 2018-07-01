from flask import render_template, request, helpers
from app import db, InvalidMediaPathException
from app.common.site.media import media_infos_by_req, make_media_file
from . import bp

@bp.app_errorhandler(400)
def bad_request_error(error):
    #if wants_json_response():
    #    return api_error_response(404)
    return render_template('error/400.html'), 400

@bp.app_errorhandler(404)
def not_found_error(error):
    media_infos = media_infos_by_req(request.path)
    if media_infos:
        try:
            path, name, content_type, bin = make_media_file(**media_infos)
            response = helpers.make_response(bin)
            if media_infos['type'] == 'photo':
                response.headers['Content-type'] = content_type
            return response
        except InvalidMediaPathException as e:
            return render_template('error/400.html'), 400

    #if wants_json_response():
    #    return api_error_response(404)
    return render_template('error/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    #if wants_json_response():
    #    return api_error_response(500)
    return render_template('error/500.html'), 500
