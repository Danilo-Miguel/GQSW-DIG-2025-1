from flask import Blueprint, request, jsonify
from app.models.user import User, db  # Importando o modelo de usuário e db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity  # Importando funções do JWT
from app import jwt  # Importando o JWTManager

# Criando o Blueprint para autenticação
auth_bp = Blueprint("auth", __name__)

# Rota de registro de usuário
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json  # Obtendo os dados da requisição (nome, e-mail, senha)
    
    # Verificando se o e-mail já existe no banco de dados
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 400  # Retorna erro caso já exista

    # Criando o novo usuário
    user = User(name=data["name"], email=data["email"])
    user.set_password(data["password"])  # Criptografando a senha
    db.session.add(user)  # Adicionando o usuário à sessão do banco de dados
    db.session.commit()  # Confirmando a transação no banco de dados

    return jsonify({"message": "User created successfully"}), 201  # Retorna sucesso

# Rota de login de usuário
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json  # Obtendo os dados de login (e-mail, senha)
    user = User.query.filter_by(email=data["email"]).first()  # Buscando o usuário pelo e-mail

    if user and user.check_password(data["password"]):  # Verificando se a senha está correta
        token = create_access_token(identity=user.id)  # Criando o token JWT
        return jsonify({"token": token}), 200  # Retorna o token JWT

    return jsonify({"error": "Invalid credentials"}), 401  # Retorna erro caso as credenciais estejam incorretas

# Rota de logout de usuário
@auth_bp.route("/logout", methods=["POST"])
@jwt_required()  # Exige que o usuário esteja autenticado (token válido)
def logout():
    return jsonify({"message": "Logout successful"}), 200  # Retorna mensagem de sucesso
