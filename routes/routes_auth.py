# Nas rotas, em projetos profissionais, normalmente as funções onde são feitos todos os processos, são importados todos pelo "service", e não um por um.
# E então na rota, a FUNÇÃO DA ROTA sempre buscar ser um nome curto e diferente da função que chamamos. Como podemos ver na rota "/usuarios" (GET), 
# retornamos service_auth.listar_usuarios(), e na rota "/usuarios" (POST), service_auth.registrar_usuario().

# ====================================================================FRAMEWORK====================================================================
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

# ===================================================================SERVICE/AUTH==================================================================
from Projeto_ORM.services import service_auth

auth_bp = Blueprint("auth", __name__, url_prefix='/auth')

# # ====================================================================ROTAS======================================================================
@auth_bp.route('/adicionar', methods=['POST'])
def adicionar_usuario():
    data = request.get_json() # Na rota procuramos sempre receber os dados JSON do usuário, pois o Service, quanto mais apenas objetos Python melhor.
    return service_auth.registrar_usuario(data)

@auth_bp.route('/login', methods=['POST'])
def token():
    data = request.get_json()
    return service_auth.login(data)