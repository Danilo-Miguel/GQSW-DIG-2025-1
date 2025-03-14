from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager  # Importando o JWTManager

# Instâncias globais para o banco de dados, bcrypt e jwt
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()  # Instância do JWTManager

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados, Bcrypt e JWT
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Usando banco SQLite local
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita modificações de rastreamento (não é necessário)
    app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'  # Definindo a chave secreta para gerar tokens JWT

    # Inicializa o SQLAlchemy, Bcrypt e JWTManager com a aplicação
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)  # Inicializando o JWTManager com a app

    # Registrando Blueprints (rotas)
    from .routes.auth import auth_bp  # Importando o Blueprint de autenticação
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Registrando a rota de autenticação com prefixo '/auth'

    return app  # Retornando a instância da aplicação