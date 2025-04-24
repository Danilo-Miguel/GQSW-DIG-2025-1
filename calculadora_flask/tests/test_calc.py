# test_calc.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importando as funções de cálculo do módulo 'calc'
from calc import somar, subtrair, multiplicar, dividir

# Função de teste para a operação de soma
def test_somar():
    # Verifica se a soma de 2 e 3 é igual a 5
    assert somar(2, 3) == 5
    # Verifica se a soma de -1 e 1 é igual a 0
    assert somar(-1, 1) == 0

# Função de teste para a operação de subtração
def test_subtrair():
    # Verifica se a subtração de 5 e 3 é igual a 2
    assert subtrair(5, 3) == 2
    # Verifica se a subtração de 0 e 4 é igual a -4
    assert subtrair(0, 4) == -4

# Função de teste para a operação de multiplicação
def test_multiplicar():
    # Verifica se a multiplicação de 2 e 3 é igual a 6
    assert multiplicar(2, 3) == 6
    # Verifica se a multiplicação de 0 e 10 é igual a 0
    assert multiplicar(0, 10) == 0

# Função de teste para a operação de divisão
def test_dividir():
    # Verifica se a divisão de 10 por 2 é igual a 5
    assert dividir(10, 2) == 5
    # Verifica se a divisão de 5 por 2 é igual a 2.5
    assert dividir(5, 2) == 2.5

# Função de teste para verificar a divisão por zero
def test_dividir_por_zero():
    # Verifica se a divisão por zero retorna a mensagem de erro correta
    assert dividir(10, 0) == "Erro: divisão por zero"