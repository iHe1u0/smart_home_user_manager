from enum import Enum


class ErrorCode(Enum):
    SUCCESS = (200, "Success")
    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORIZED = (401, "Unauthorized")
    ACCOUNT_EXISTS = (4001, "Account already exists")  # 自定义错误码
    MISSING_PARAMS = (4002, "Missing account or password")
    SERVER_ERROR = (500, "Internal Server Error")

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def to_dict(self):
        return {"code": self.code, "message": self.message}
