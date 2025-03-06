from flask import Blueprint, request, jsonify
from app.models.user import User, db
from flask_jwt_extended import create_access_token, jwt_required
from app import jwt  # Importando o JWTManager

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(name=data["name"], email=data["email"])
    user.set_password(data["password"])  # Definindo a senha com hash
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)  # Criando o token
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify({"message": "Logout successful"}), 200
