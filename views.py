from flask import Blueprint

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/index/')
def index():
    return 'This is flask blueprint example'
