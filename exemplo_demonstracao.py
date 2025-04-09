"""Módulo de demonstração de boas práticas com operações matemáticas simples."""

def calcula(valor1, valor2, operacao):
    """
    Realiza uma operação matemática com dois valores.

    Parâmetros:
    valor1 (float): Primeiro valor numérico.
    valor2 (float): Segundo valor numérico.
    operacao (str): Tipo de operação: 'soma', 'subtrai', 'multiplica' ou 'divide'.

    Retorna:
    None
    """
    if operacao == "soma":
        resultado = valor1 + valor2
        print("O resultado é:", resultado)
    elif operacao == "subtrai":
        resultado = valor1 - valor2
        print("O resultado é:", resultado)
    elif operacao == "multiplica":
        resultado = valor1 * valor2
        print("O resultado é:", resultado)
    elif operacao == "divide":
        if valor2 != 0:
            resultado = valor1 / valor2
            print("O resultado é:", resultado)
        else:
            print("Não é possível dividir por zero")
    else:
        print("Operação inválida")


def main():
    """
    Executa exemplos da função calcula com diferentes operações.
    """
    calcula(10, 2, "soma")
    calcula(10, 2, "subtrai")
    calcula(10, 2, "multiplica")
    calcula(10, 0, "divide")
    calcula(10, 2, "exponencia")

main()
