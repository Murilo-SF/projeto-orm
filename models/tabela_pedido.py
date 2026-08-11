from Projeto_ORM.extensions import db

# ======================================================================TABELA PEDIDO======================================================================
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    valor = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id_usuario":self.cliente_id,
            "id_pedido": self.id,
            "valor": self.valor
         }