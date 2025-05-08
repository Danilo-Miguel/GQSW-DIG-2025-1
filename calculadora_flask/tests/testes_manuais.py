import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests/test_calc.py

from calc import somar, subtrair, multiplicar, dividir

def testar_operacoes():
    print("=== Teste Manual ===")

    # Soma
    print("Soma:")
    print("2 + 3 =", somar(2, 3))        # Esperado: 5
    print("-1 + 1 =", somar(-1, 1))      # Esperado: 0
    print()

    # Subtração
    print("Subtração:")
    print("5 - 3 =", subtrair(5, 3))     # Esperado: 2
    print("0 - 0 =", subtrair(0, 0))     # Esperado: 0
    print()

    # Multiplicação
    print("Multiplicação:")
    print("2 * 3 =", multiplicar(2, 3))  # Esperado: 6
    print("0 * 5 =", multiplicar(0, 5))  # Esperado: 0
    print()

    # Divisão
    print("Divisão:")
    print("6 / 3 =", dividir(6, 3))      # Esperado: 2
    print("5 / 0 =", dividir(5, 0))      # Esperado: 'Erro: divisão por zero'
    print()

testar_operacoes()
