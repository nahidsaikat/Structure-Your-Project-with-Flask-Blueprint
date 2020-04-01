from flask import Flask, Blueprint

from .extensions import db, ma
from app.note.views import note_blueprint



def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(note_blueprint)

    return app
