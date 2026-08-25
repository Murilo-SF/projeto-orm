# =====================================================================FRAMEWORK=====================================================================
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

# ===================================================================BANCO DE DADOS==================================================================
from Projeto_ORM.extensions import db

# ======================================================================TABELAS======================================================================
from Projeto_ORM.models.tabela_usuario import Usuario
from Projeto_ORM.models.tabela_pedido import Pedido

# ======================================================================SCHEMAS======================================================================
from Projeto_ORM.schemas.schema_usuario import schema_usuario
from Projeto_ORM.schemas.schema_pedido import schema_pedido

# =======================================================================ERRORS=======================================================================
from Projeto_ORM.errors.handlers import UsuarioNaoEncontrado, PedidoNaoEncontrado

# ===================================================================SERVICE/PEDIDO===================================================================
# ================================================================Buscar Pedidos/admin================================================================
def listar_pedidos_admin(cliente_id):
    
    usuario = db.session.get(Usuario, cliente_id)
    if not usuario:
        raise UsuarioNaoEncontrado()

    pedidos = usuario.pedidos
    return jsonify ({"nome":usuario.nome, "id_cliente":usuario.id, "pedidos":[pedido.to_dict() for pedido in pedidos]}), 200

# ===================================================================Buscar Pedidos===================================================================
def listar_pedidos(cliente_id):

    usuario = db.session.get(Usuario, cliente_id)
    if not usuario:
        raise UsuarioNaoEncontrado()

    pedidos = usuario.pedidos
    return jsonify ({"nome":usuario.nome, "id_cliente":usuario.id, "pedidos":[pedido.to_dict() for pedido in pedidos]}), 200

# ==================================================================Adicionar Pedido==================================================================
def registrar_pedido(data):
    
    data = schema_pedido.load(data)

    cliente_id = data.get('cliente_id')
    valor = data.get('valor')

    if not Usuario.query.filter_by(id=cliente_id).first():
        raise UsuarioNaoEncontrado()
    
    novo_pedido = Pedido(cliente_id=cliente_id, valor=valor)
    db.session.add(novo_pedido)
    db.session.flush()

    return jsonify ({"message":"Pedido cadastrado com sucesso!", "pedido": novo_pedido.to_dict()}), 201

# =================================================================Atualizar Pedido=================================================================
def atualizar_pedido(id_pedido, data):

    pedido = db.session.get(Pedido, id_pedido)

    if not pedido:
        raise PedidoNaoEncontrado()
    
    pedido.cliente_id = data.get('cliente_id', pedido.cliente_id)
    pedido.valor = data.get('valor', pedido.valor)

    db.session.flush()    

    return jsonify ({"message":"Pedido cadastrado com sucesso!", "pedido": pedido.to_dict()}), 200

# ==================================================================Deletar Pedido==================================================================
def deletar_pedido(id_pedido):

    pedido = db.session.get(Pedido, id_pedido)

    if not pedido:
        raise PedidoNaoEncontrado()
    
    db.session.delete(pedido)
    db.session.flush()

    return jsonify ({"message": "Pedido deletado com sucesso!"}), 200