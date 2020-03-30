from flask import Blueprint, request, jsonify

from app import db
from src.note.models import NoteModel
from src.note.schemas import NoteSchema


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
note_blueprint = Blueprint('note_blueprint', __name__)


@note_blueprint.route('/')
def hello_world():
    return 'Hello, World!'


@note_blueprint.route('/note/')
def note_list():
    all_notes = NoteModel.query.all()
    return jsonify(notes_schema.dump(all_notes))


@note_blueprint.route('/note/', methods=['POST'])
def create_note():
    title = request.json.get('title', '')
    content = request.json.get('content', '')

    note = NoteModel(title=title, content=content)
    
    db.session.add(note)
    db.session.commit()
    
    return note_schema.jsonify(note)


@note_blueprint.route('/note/<int:note_id>/', methods=["GET"])
def note_detail(note_id):
    note = NoteModel.query.get(note_id)
    return note_schema.jsonify(note)


@note_blueprint.route('/note/<int:note_id>/', methods=['PATCH'])
def update_note(note_id):
    title = request.json.get('title', '')
    content = request.json.get('content', '')

    note = NoteModel.query.get(note_id)
    
    note.title = title
    note.content = content

    db.session.add(note)
    db.session.commit()

    return note_schema.jsonify(note)


@note_blueprint.route('/note/<int:note_id>/', methods=["DELETE"])
def delete_note(note_id):
    note = NoteModel.query.get(note_id)
    
    db.session.delete(note)
    db.session.commit()

    return note_schema.jsonify(note)
