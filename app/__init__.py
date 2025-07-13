# Where your Flask app and DB are initialized
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
