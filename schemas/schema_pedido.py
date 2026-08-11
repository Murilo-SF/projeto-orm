from marshmallow import Schema, fields
from marshmallow.validate import Length

# ===================================================================SCHEMA/PEDIDO===================================================================
class PedidoSchema(Schema):
    cliente_id = fields.Integer(required=True)
    valor = fields.Float(required=True)

schema_pedido = PedidoSchema()