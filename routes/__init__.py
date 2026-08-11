from Projeto_ORM.routes.routes_auth import auth_bp
from Projeto_ORM.routes.routes_usuario import usuario_bp
from Projeto_ORM.routes.routes_pedido import pedido_bp

def register_blueprints(aplicativo):
    aplicativo.register_blueprint(auth_bp)
    aplicativo.register_blueprint(usuario_bp)
    aplicativo.register_blueprint(pedido_bp)