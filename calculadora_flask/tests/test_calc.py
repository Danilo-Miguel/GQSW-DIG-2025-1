import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests/test_calc.py

import pytest
from calc import somar, subtrair, multiplicar, dividir

# Teste de somar com parametrize
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-1, -1, -2),
    (2.5, 3.5, 6.0),
])
def test_somar_parametrize(a, b, esperado):
    assert somar(a, b) == esperado

# Teste de subtrair com parametrize
@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (5.5, 2.2, 3.3),
])
def test_subtrair_parametrize(a, b, esperado):
    assert subtrair(a, b) == esperado

# Teste de multiplicar com parametrize
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 5, 0),
    (-1, -1, 1),
    (2.5, 4.0, 10.0),
])
def test_multiplicar_parametrize(a, b, esperado):
    assert multiplicar(a, b) == esperado

# Teste de dividir com parametrize (divisões válidas)
@pytest.mark.parametrize("a, b, esperado", [
    (6, 3, 2),
    (0, 5, 0),
    (-6, -3, 2),
    (7.5, 2.5, 3.0),
])
def test_dividir_parametrize(a, b, esperado):
    assert dividir(a, b) == esperado

# Teste de dividir por zero (divisões inválidas que retornam erro)
@pytest.mark.parametrize("a, b", [
    (5, 0),
    (0, 0),
])
def test_dividir_por_zero_parametrize(a, b):
    assert dividir(a, b) == 'Erro: divisao por zero'
