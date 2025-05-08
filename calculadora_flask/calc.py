# calc.py

# This is a simple calculator program that performs basic arithmetic operations.
# It includes functions for addition, subtraction, multiplication, and division.
# Each function takes two arguments and returns the result of the operation.

# This function takes two numbers and returns their sum.
def somar(a, b):
    return a + b

# This function takes two numbers and returns their difference.
def subtrair(a, b):
    return a - b

# This function takes two numbers and returns their product.
def multiplicar(a, b):
    return a * b

# This function takes two numbers and returns their quotient.
# If the second number is zero, it returns 'undefined' to avoid division by zero.
def dividir(a, b):
    if b == 0:
        return "Undefined" #return 'Erro: divisao por zero' # This line is commented out to avoid division by zero error.
    else:
        return a / b 