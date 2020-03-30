import os

from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from src.note.views import note_blueprint

app = Flask(__name__)

app.register_blueprint(note_blueprint)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
                os.path.join(basedir, 'db.sqlite3')

db = SQLAlchemy(app)
ma = Marshmallow(app)


if __name__ == '__main__':
    app.run(debug=True)
