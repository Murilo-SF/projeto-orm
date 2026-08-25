from Projeto_ORM.extensions import db

def init_transaction(app):
    @app.teardown_request    
    def finalizar_transacao(exception):

        if exception is not None: # Se existir uma exceção
            db.session.rollback()
        elif not app.config["TESTING"]: # Se a configuração de criação do app NÃO for de testes:
            db.session.commit()