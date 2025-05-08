import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calc import somar, subtrair, multiplicar, dividir

# Test cases for the calculator functions

# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 5),
#     (-1, 1, 0),
#     (0, 0, 0),
#     (-1, -1, -2)
# ])

# def test_somar_parametrizado(a, b, expected):
#     assert somar(a, b) == expected


# @pytest.mark.parametrize("a, b", [
#     (5, 0),
#     (0, 0)  
# ])   

# def test_dividir_parametrize(a, b):
#     assert dividir(a, b) == 'Undefined'  # Verifica se a divisão por zero retorna 'undefined'



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

# def test_dividir():
#     assert dividir(6, 3) == 2
#     assert dividir(0, 5) == 0
#     assert dividir(-6, -3) == 2
#     assert dividir(5, 0) == 'Undefined'  # Verifica se a divisão por zero retorna 'undefined'
#     assert dividir(0, 0) == 'Undefined' 

# def test_tipo_retorno_dividir():

#     resultado = dividir(6, 3)
#     assert isinstance(resultado, (int, float))  # Verifica se o retorno é do tipo int ou float quando a divisão é válida


#     resultado = dividir(5, 0)
#     assert isinstance(resultado, str)  # Verifica se o retorno é do tipo str(String) quando a divisão é indefinida

# def teste_undefined():
#     assert dividir(5, 0) == 'Undefined'
#     assert dividir(0, 0) == 'Undefined'  # Verifica se a divisão por zero retorna 'undefined'    

def test_somar_floats():
    assert somar(2.5, 3.5) == 6.0
    assert somar(-1.5, 1.5) == 0.0
    assert somar(0.0, 0.0) == 0.0
    assert somar(-1.5, -1.5) == -3.0

def test_subtrair_floats():
    assert subtrair(5.5, 3.5) == 2.0
    assert subtrair(0.0, 0.0) == 0.0
    assert subtrair(-1.5, -1.5) == 0.0
    assert subtrair(-1.5, 1.5) == -3.0      

def test_multiplicar_floats():
    assert multiplicar(2.5, 3.5) == 8.75
    assert multiplicar(-1.5, 1.5) == -2.25
    assert multiplicar(0.0, 5.0) == 0.0
    assert multiplicar(-1.5, -1.5) == 2.25

# def test_dividir_floats():
#     assert dividir(6.5, 3.5) == 1.8571428571428572
#     assert dividir(0.0, 5.0) == 0.0
#     assert dividir(-6.5, -3.5) == 1.8571428571428572
#     assert dividir(5.0, 0.0) == 'Undefined'  # Verifica se a divisão por zero retorna 'undefined'
#     assert dividir(0.0, 0.0) == 'Undefined' # Verifica se a divisão por zero retorna 'undefined'    

