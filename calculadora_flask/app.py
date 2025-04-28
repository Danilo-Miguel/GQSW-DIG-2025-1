#app.py

from flask import Flask, request, render_template
from calc import somar, subtrair, multiplicar, dividir

app = Flask(__name__)

# Define a route for the calculator page
# This route handles both GET and POST requests.
@app.route('/calculadora', methods=['GET', 'POST'])
def index():
    resultado = None

# Check if the request method is POST
# If it is, retrieve the input values and perform the selected operation.
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            operacao = request.form['operacao']

            if operacao == 'somar':
                resultado = somar(a, b)
            elif operacao == 'subtrair':
                resultado = subtrair(a, b)
            elif operacao == 'multiplicar':
                resultado = multiplicar(a, b)
            elif operacao == 'dividir':
                resultado = dividir(a, b)
        except Exception as e:
                resultado = 'Erro: ' + str(e)

    return render_template('index.html', resultado=resultado)          

if __name__ == '__main__':
    app.run(debug=True)  
