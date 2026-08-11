# =====================================================================FRAMEWORK=====================================================================
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# =====================================================================DECORATORS====================================================================
from Projeto_ORM.decorators.auth_decorators import role_required

# ===================================================================SERVICE/USUARIO=================================================================
from Projeto_ORM.services import service_usuario

usuario_bp = Blueprint("usuario", __name__, url_prefix='/usuario')

# =======================================================================ROTAS=======================================================================
@usuario_bp.route('/me', methods=['GET'])
@jwt_required()
def buscar_usuario_id():
    id_usuario = get_jwt_identity()
    return service_usuario.buscar_usuario(id_usuario)

@usuario_bp.route('/todos', methods=['GET'])
@role_required("admin")
def usuarios():
    return service_usuario.listar_usuarios()

@usuario_bp.route('/admin')
@role_required("admin")
def admin():
    return service_usuario.admin()

@usuario_bp.route('/atualizar/<int:id_usuario>', methods=['PUT'])
@role_required("admin")
def atualizar_usuario(id_usuario):
    data = request.get_json()
    return service_usuario.atualizar_usuario(id_usuario, data)

@usuario_bp.route('/deletar/<int:id_usuario>', methods=['DELETE'])
@role_required("admin")
def deletar_usuario(id_usuario):
    return service_usuario.deletar_usuario(id_usuario)