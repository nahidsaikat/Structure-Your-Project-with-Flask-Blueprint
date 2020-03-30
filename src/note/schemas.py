from app import ma
from src.note.models import NoteModel


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NoteModel
