from app import create_app, db
# comentários
app = create_app()

# Criação do banco de dados (tabelas)
with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados

if __name__ == '__main__':
    app.run(debug=True)  # Roda a aplicação Flask com modo debug ativado