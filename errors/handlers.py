from marshmallow import ValidationError
from flask import jsonify
from Projeto_ORM.errors.exceptions import UsuarioNaoEncontrado, UsuarioJaExiste, PedidoNaoEncontrado, SenhaIncorreta

def register_error_handlers(aplicativo):

    @aplicativo.errorhandler(UsuarioNaoEncontrado)
    def usuario_nao_encontrado(error):
        return jsonify ({"error":"Usuário não encontrado!"}), 404

    @aplicativo.errorhandler(PedidoNaoEncontrado)
    def pedido_nao_encontrado(error):
        return jsonify ({"error":"Pedido não encontrado!"}), 404
    
    @aplicativo.errorhandler(UsuarioJaExiste)
    def usuario_ja_existe(error):
        return jsonify ({"error":"Usuário já existe!"}), 400
    
    @aplicativo.errorhandler(ValidationError)
    def pedido_nao_encontrado(error):
        return jsonify ({"error":error.messages}), 400
    
    @aplicativo.errorhandler(SenhaIncorreta)
    def senha_incorreta(error):
        return jsonify ({"error":"SENHA INCORRETA!"}), 400