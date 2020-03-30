import os

from flask import Flask
from src.views import note_blueprint

app = Flask(__name__)

app.register_blueprint(note_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
