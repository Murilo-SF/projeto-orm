# =====================================================================FRAMEWORK=====================================================================
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
# ===================================================================BANCO DE DADOS==================================================================
from Projeto_ORM.extensions import db

# ======================================================================TABELAS======================================================================
from Projeto_ORM.models.tabela_usuario import Usuario
from Projeto_ORM.models.tabela_pedido import Pedido

# ======================================================================SCHEMAS======================================================================
from Projeto_ORM.schemas.schema_usuario import schema_usuario

# ============================================================FRAMEWORK WERKZEUG/SECURITY============================================================
from werkzeug.security import generate_password_hash, check_password_hash

# ======================================================================ERRORS=======================================================================
from Projeto_ORM.errors.handlers import UsuarioNaoEncontrado, UsuarioJaExiste, SenhaIncorreta

# ===================================================================SERVICES/AUTH===================================================================
# =================================================================Registrar Usuario=================================================================
def registrar_usuario(data):
    data = schema_usuario.load(data)

    nome = data.get('nome')
    senha = data.get('senha')
    role = data.get('role')
    email = data.get('email', "NULL")

    if Usuario.query.filter_by(nome=nome).first():
        raise UsuarioJaExiste()
    
    novo_usuario = Usuario(nome=nome, senha=generate_password_hash(senha), role=role, email=email)
    db.session.add(novo_usuario)
    db.session.flush()

    return jsonify ({"message":"Usuário cadastrado com sucesso!", "usuario":novo_usuario.to_dict()}), 201

# =====================================================================Login========================================================================
def login(data):
    data = schema_usuario.load(data)

    nome = data.get('nome')
    senha = data.get('senha')

    usuario = Usuario.query.filter_by(nome=nome).first()

    if not usuario:
        raise UsuarioNaoEncontrado()
    
    if not check_password_hash(usuario.senha, senha):
        raise SenhaIncorreta()
    
    token = create_access_token(identity=str(usuario.id), additional_claims={"nome":usuario.nome,"role":usuario.role})
    
    return jsonify ({"token":token}), 201