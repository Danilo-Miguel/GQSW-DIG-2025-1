import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# tests/testes_manuais.py

from calc import somar, subtrair, multiplicar, dividir
# Teste de somar

def testar_operacoes():

    # Teste de somar
    print("Teste de soma:")

    print("2 + 3 =", somar(2, 3))
    print("-1 + 1 =", somar(-1, 1))
    print("0 + 0 =", somar(0, 0))
    print("-1 + -1 =", somar(-1, -1))
    print("2.5 + 3.5 =", somar(2.5, 3.5))

    # Teste de subtrair
    print("\nTeste de subtração:")

    print("5 - 3 =", subtrair(5, 3))
    print("0 - 0 =", subtrair(0, 0))
    print("-1 - -1 =", subtrair(-1, -1))
    print("-1 - 1 =", subtrair(-1, 1))
    print("5.5 - 2.2 =", subtrair(5.5, 2.2))

    # Teste de multiplicar
    print("\nTeste de multiplicação:")
    print("2 * 3 =", multiplicar(2, 3))
    print("-1 * 1 =", multiplicar(-1, 1))
    print("0 * 5 =", multiplicar(0, 5))
    print("-1 * -1 =", multiplicar(-1, -1))
    print("2.5 * 4.0 =", multiplicar(2.5, 4.0))

    # Teste de dividir
    print("\nTeste de divisão:")
    print("6 / 3 =", dividir(6, 3))
    print("0 / 5 =", dividir(0, 5))
    print("-6 / -3 =", dividir(-6, -3))
    print("7.5 / 2.5 =", dividir(7.5, 2.5))

testar_operacoes()