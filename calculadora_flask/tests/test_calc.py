import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calc import somar, subtrair, multiplicar, dividir

# Test cases for the calculator functions
def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0
    assert somar(-1, -1) == -2

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 0) == 0
    assert subtrair(-1, -1) == 0
    assert subtrair(-1, 1) == -2

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0
    assert multiplicar(-1, -1) == 1

def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(0, 5) == 0
    assert dividir(-6, -3) == 2
    assert dividir(5, 0) == 'undefined'
    assert dividir(0, 0) == 'undefined' 

def test_tipo_retorno_dividir():
    resultado = dividir(6, 3)
    assert isinstance(resultado, (int, float))  # Verifica se o resultado é um número
    
    resultado = dividir(6, 0)
    assert isinstance(resultado, str)  # Verifica se o resultado é uma string quando a divisão é inválida(Divisão por zero retorno string)
 

     