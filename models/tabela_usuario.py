from Projeto_ORM.extensions import db

# ======================================================================TABELA USUARIO======================================================================
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), nullable=True)

    pedidos = db.relationship('Pedido', backref='usuarios', lazy=True)

    def to_dict(self):
        return {
            "nome": self.nome,
            "id": self.id,
            "role": self.role,
            "email":self.email
        }