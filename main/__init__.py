from flask import Flask, jsonify

from api import api_bp, db


def handle_error(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "The requested URL was not found on the server."
        }), 404


def create_app():
    app = Flask(__name__, template_folder='template')
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql://smart_home:H4pRMfycYZ6wKmKr@192.168.0.109/smart_home'  # Update your DB URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # 注册API蓝图
    app.register_blueprint(api_bp, url_prefix='/api')

    handle_error(app)

    return app
