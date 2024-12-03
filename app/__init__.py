from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'db/app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Importar e registrar rotas
    from .routes import routes
    app.register_blueprint(routes)

    return app
