"Este módulo contém funções para demonstração de boas práticas de código."

def calcula(valor1, valor2, operacao):
    "Essa função contém os calculos de soma, subtração, multiplicação e divisão."
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
    "Essa função chama a função calcula com diferentes operações."
    calcula(10, 2, "soma")
    calcula(10, 2, "subtrai")
    calcula(10, 2, "multiplica")
    calcula(10, 0, "divide")
    calcula(10, 2, "exponencia")

main()
