from app.extensions import ma
from app.note.models import NoteModel


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NoteModel
