from app import db, bcrypt  # Importando a instância do db e bcrypt
from flask_bcrypt import Bcrypt

class User(db.Model):  # Definindo a tabela User
    id = db.Column(db.Integer, primary_key=True)  # ID do usuário, chave primária
    name = db.Column(db.String(100), nullable=False)  # Nome do usuário
    email = db.Column(db.String(120), unique=True, nullable=False)  # E-mail único do usuário
    password = db.Column(db.String(255), nullable=False)  # Senha do usuário (será criptografada)

    def set_password(self, password):
        """Método para criptografar a senha antes de salvar"""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Método para comparar a senha fornecida com a senha criptografada"""
        return bcrypt.check_password_hash(self.password, password)
