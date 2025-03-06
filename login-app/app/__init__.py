from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager  # Importar o JWTManager

# Instâncias globais
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()  # Instância do JWTManager

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados e JWT
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'

    # Inicializa o SQLAlchemy e Bcrypt
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)  # Inicializando o JWTManager com a app

    # Registrando Blueprints (rotas)
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
