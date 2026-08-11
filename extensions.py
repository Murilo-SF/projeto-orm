from flask_sqlalchemy import SQLAlchemy

# Estudando as "extensões" dessa forma, assim podemos reutilizar sempre que quisermos.

db = SQLAlchemy() # Agora não passamos mais o app como objeto, pois depois vamos inicar a base de dados utilizando db.init_app(aplicativo).
# Dessa forma podemos reutilizar o objeto, como por ex, quando quisermos testar em um Banco de Dados teste.