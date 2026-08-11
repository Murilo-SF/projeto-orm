# ====================================================================FRAMEWORK====================================================================
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

# =====================================================================DECORATORS==================================================================
from Projeto_ORM.decorators.auth_decorators import role_required

# ==================================================================SERVICE/PEDIDO=================================================================
from Projeto_ORM.services import service_pedido 

pedido_bp = Blueprint("pedido", __name__, url_prefix='/pedido')

# =====================================================================ROTAS=======================================================================
@pedido_bp.route('/<int:usuario_id>', methods=['GET'])
@role_required("admin")
def buscar_pedidos_admin(usuario_id):
    return service_pedido.listar_pedidos_admin(usuario_id)

@pedido_bp.route('/me', methods=['GET'])
@jwt_required()
def buscar_pedidos():
    id_usuario = get_jwt_identity()
    return service_pedido.listar_pedidos(id_usuario)

@pedido_bp.route('/adicionar', methods=['POST'])
def adicionar_pedido():
    data = request.get_json()
    return service_pedido.registrar_pedido(data)

@pedido_bp.route('/atualizar/<int:id_pedido>', methods=['PUT'])
@role_required("admin")
def atualizar_pedido(id_pedido):
    data = request.get_json()
    return service_pedido.atualizar_pedido(id_pedido, data)

@pedido_bp.route('/deletar/<int:id_pedido>', methods=['DELETE'])
@role_required("admin")
def deletar_pedido(id_pedido):
    return service_pedido.deletar_pedido(id_pedido)