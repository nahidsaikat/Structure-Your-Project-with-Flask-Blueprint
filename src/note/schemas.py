from flask_marshmallow import Marshmallow
from app import app

ma = Marshmallow(app)


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NoteModel
