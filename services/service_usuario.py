# =====================================================================FRAMEWORK=====================================================================
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash

# ===================================================================BANCO DE DADOS==================================================================
from Projeto_ORM.extensions import db

# ======================================================================TABELAS======================================================================
from Projeto_ORM.models.tabela_usuario import Usuario
from Projeto_ORM.models.tabela_pedido import Pedido

# ======================================================================SCHEMAS======================================================================
from Projeto_ORM.schemas.schema_usuario import schema_usuario

# ======================================================================ERRORS=======================================================================
from Projeto_ORM.errors.handlers import UsuarioNaoEncontrado, UsuarioJaExiste

# ===================================================================SERVICE/USUARIO=================================================================
# ===================================================================Listar Usuários=================================================================
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify ({"usuarios":[usuario.to_dict() for usuario in usuarios]}), 200

# =======================================================================Admin=======================================================================
def admin():
    return jsonify ({"message": "Bem-vindo Administrador!"}), 200

# ==================================================================Buscar Usuário===================================================================
def buscar_usuario(id_usuario):
    
    usuario = db.session.get(Usuario, id_usuario)

    if not usuario:
        raise UsuarioNaoEncontrado()
    
    return jsonify ({"user": usuario.to_dict()}), 200

# =================================================================Atualizar Usuário=================================================================
def atualizar_usuario(id, data):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    senha = data.get('senha')

    if senha:
        usuario.senha = generate_password_hash(data.get('senha'))

    usuario.nome = data.get('nome', usuario.nome)
    usuario.role = data.get('role', usuario.role)
    usuario.email = data.get('email', usuario.email)

    db.session.commit()

    return jsonify ({"message":"Usuário atualizado com sucesso!", "usuario":usuario.to_dict()}), 200

# ==================================================================Deletar Usuário==================================================================
def deletar_usuario(id):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()
    
    db.session.delete(usuario)
    db.session.commit()

    return jsonify ({"message":"Usuário deletado com sucesso!"}), 200