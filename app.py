from flask import Flask
from views import index_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
