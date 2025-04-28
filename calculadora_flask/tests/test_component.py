# tests/test_component.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests/test_calc.py

import pytest
from app import app  # importa o app Flask

from calc import somar, subtrair, multiplicar, dividir

# Usamos a fixture do Flask para testar a aplicação sem rodar o servidor real
@pytest.fixture
def client():
    app.config['TESTING'] = True  # coloca o app no modo de teste
    with app.test_client() as client:
        yield client

# Testar se GET /calculadora carrega a página
def test_get_calculadora(client):
    response = client.get('/calculadora')
    assert response.status_code == 200  # Status OK
    assert b'Calculadora Simples' in response.data  # Verifica se o título aparece no HTML

# Testar operação de soma (POST)
def test_post_somar(client):
    response = client.post('/calculadora', data={'a': '5', 'b': '3', 'operacao': 'somar'})
    assert response.status_code == 200
    assert b'Resultado: 8.0' in response.data  # 5 + 3 = 8.0 (float porque input step=any)

# Testar operação de subtração (POST)
def test_post_subtrair(client):
    response = client.post('/calculadora', data={'a': '10', 'b': '4', 'operacao': 'subtrair'})
    assert response.status_code == 200
    assert b'Resultado: 6.0' in response.data  # 10 - 4 = 6.0

# Testar operação de multiplicação (POST)
def test_post_multiplicar(client):
    response = client.post('/calculadora', data={'a': '7', 'b': '6', 'operacao': 'multiplicar'})
    assert response.status_code == 200
    assert b'Resultado: 42.0' in response.data  # 7 * 6 = 42.0

# Testar operação de divisão (POST)
def test_post_dividir(client):
    response = client.post('/calculadora', data={'a': '8', 'b': '2', 'operacao': 'dividir'})
    assert response.status_code == 200
    assert b'Resultado: 4.0' in response.data  # 8 / 2 = 4.0

# Testar divisão por zero (POST)
def test_post_dividir_por_zero(client):
    response = client.post('/calculadora', data={'a': '5', 'b': '0', 'operacao': 'dividir'})
    assert response.status_code == 200
    assert b'Erro: divisao por zero' in response.data  # Testar mensagem de erro
