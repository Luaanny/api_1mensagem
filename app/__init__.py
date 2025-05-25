from flask import Flask
from .config import Config
from app.db import db, migrate
from app.models import mensagens

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.json.sort_keys = False
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.mensagens_routes import messages_bp
    app.register_blueprint(messages_bp, url_prefix='/mensagens')

    return app