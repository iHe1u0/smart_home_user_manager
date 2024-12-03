from flask import jsonify

def make_response(error_code, data=None):
    """
    统一返回格式，支持 ErrorCode 枚举
    """
    response = {
        "code": error_code.code,
        "message": error_code.message,
    }
    if data is not None:
        response["data"] = data
    return jsonify(response), error_code.code
