import os

from flask import Flask, Blueprint

from .extensions import db, ma
from app.note.views import note_blueprint


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(BASE_DIR, 'db.sqlite3')

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(note_blueprint)

    return app
