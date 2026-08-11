#========================================================================CONFIG BASE========================================================================
class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    # Por quê desabilitar isto? Consome espaço aditional de memória e recursos da CPU.
    
#========================================================================CONFIG DEVELOPMENT========================================================================
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/empresa' # Faz a conexão com o nosso banco de dados.
    JWT_SECRET_KEY = 'chave-development-chave-development-chave-development' # Criamos a assinatura do nosso token
    DEBUG = True 

#========================================================================CONFIG TESTING========================================================================
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/empresa_test'
    JWT_SECRET_KEY = 'chave-teste-chave-teste-chave-teste'
    TESTING = True

#=======================================================================CONFIG MAP========================================================================
configs = {"development": DevelopmentConfig, 'testing': TestingConfig}