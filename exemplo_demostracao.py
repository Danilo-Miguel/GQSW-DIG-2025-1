"""Este módulo demonstra boas práticas de código com foco na redução da complexidade ciclomática."""

def somar(a, b):
    """Retorna a soma de dois valores."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois valores."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois valores."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois valores, tratando divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def calcula(valor1, valor2, operacao):
    """Executa a operação solicitada entre dois valores."""
    operacoes = {
        "soma": somar,
        "subtrai": subtrair,
        "multiplica": multiplicar,
        "divide": dividir
    }

    func = operacoes.get(operacao)
    if func:
        try:
            resultado = func(valor1, valor2)
            print("O resultado é:", resultado)
        except ValueError as e:
            print("Erro:", e)
    else:
        print("Operação inválida")

def main():
    calcula(10, 2, "soma")
    calcula(10, 2, "subtrai")
    calcula(10, 2, "multiplica")
    calcula(10, 0, "divide")
    calcula(10, 2, "exponencia")

if __name__ == "__main__":
    main()
