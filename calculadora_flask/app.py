# app.py

from flask import Flask, request, render_template
from calc import somar, subtrair, multiplicar, dividir

app = Flask(__name__)

# Rota principal (formulário da calculadora)
@app.route('/calculadora', methods=['GET', 'POST'])
def index():
    resultado = None

    # Se o formulário for enviado (POST)
    if request.method == 'POST':
        try:
            a = float(request.form['a'])  # Pega valor A do form
            b = float(request.form['b'])  # Pega valor B do form
            operacao = request.form['operacao']  # Tipo de operação

            # Seleciona a operação
            if operacao == 'somar':
                resultado = somar(a, b)
            elif operacao == 'subtrair':
                resultado = subtrair(a, b)
            elif operacao == 'multiplicar':
                resultado = multiplicar(a, b)
            elif operacao == 'dividir':
                resultado = dividir(a, b)
        except Exception as e:
            resultado = f"Erro: {str(e)}"

    # Renderiza o HTML com o resultado
    return render_template('index.html', resultado=resultado)

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
