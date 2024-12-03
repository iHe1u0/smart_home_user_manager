# api/__init__.py
from flask import Blueprint

# 创建API蓝图
api_bp = Blueprint('api', __name__)

# 导入其他模块的API路由
from .users import *
