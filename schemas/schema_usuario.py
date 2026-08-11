from marshmallow import Schema, fields
from marshmallow.validate import Length

# ===================================================================SCHEMA/USUARIO===================================================================
class UsuarioSchema(Schema):
    nome = fields.String(required=True, validate=Length(min=4))
    senha = fields.String(required=True, validate=Length(min=6))
    role = fields.String(load_default='user')
    email = fields.String(validate=Length(min=14)) 

schema_usuario = UsuarioSchema()