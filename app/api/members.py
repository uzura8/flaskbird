from flask import current_app, jsonify, request, url_for
from app import db
from app.member.models import Member
from . import bp
#from app.api.auth import token_auth
#from app.api.errors import bad_request


@bp.route('/members/<int:id>', methods=['GET'])
#@token_auth.login_required
def get_member(id):
    return jsonify(Member.query.get_or_404(id).to_dict())


@bp.route('/members', methods=['GET'])
#@token_auth.login_required
def get_members():
    param = current_app.config['PARAMS_LIST_DEFAULT'];
    page = request.args.get('page', 1, type=int)
    per_page = min(
            request.args.get('per_page', param['per_page'], type=int),
            param['per_page_max'])
    data = Member.to_collection_dict(Member.query, page,
                                    per_page, 'api.get_members')
    return jsonify(data)

