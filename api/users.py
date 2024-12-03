# api/users.py
from flask import jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

from utils.error_code import ErrorCode
from utils.response_handler import make_response
from . import api_bp  # 导入在 api/__init__.py 中定义的蓝图
from main.models import User, db


@api_bp.route("/user/login", methods=["POST"])
def login():
    data = request.get_json()
    account = data.get("account")
    password = data.get("password")

    if not account or not password:
        return make_response(ErrorCode.MISSING_PARAMS)

    user = User.query.filter_by(account=account).first()
    if user and check_password_hash(user.password, password):
        # Assuming you generate a token here for authenticated users
        return make_response(ErrorCode.SUCCESS, {"user_id": user.id})
    else:
        return make_response(ErrorCode.UNAUTHORIZED)


@api_bp.route("/user/register", methods=["POST"])
def register():
    data = request.get_json()
    account = data.get("account")
    password = data.get("password")

    if not account or not password:
        return make_response(ErrorCode.MISSING_PARAMS)

    # Check if the account already exists
    if User.query.filter_by(account=account).first():
        return make_response(ErrorCode.ACCOUNT_EXISTS)

    hashed_password = generate_password_hash(password)
    new_user = User(account=account, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return make_response(ErrorCode.SUCCESS, {"user_id": new_user.id})
    except Exception as e:
        db.session.rollback()
        return make_response(ErrorCode.SERVER_ERROR, {"error": str(e)})
