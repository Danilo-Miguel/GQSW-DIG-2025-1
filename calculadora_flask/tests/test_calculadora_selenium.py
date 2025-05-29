from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Caminho para o chromedriver
caminho_driver = "D:/Documentos/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(caminho_driver)
driver = webdriver.Chrome(service=service)

# Abre a aplicação
driver.get("http://127.0.0.1:5000/calculadora")
time.sleep(2)  # Espera inicial

# Lista completa de testes: (a, b, operação, resultado esperado)
casos_de_teste = [
    # SOMA
    ("2", "3", "somar", "Resultado: 5.0"),
    ("-1", "1", "somar", "Resultado: 0.0"),
    ("0", "0", "somar", "Resultado: 0.0"),
    ("-1", "-1", "somar", "Resultado: -2.0"),
    ("2.5", "3.5", "somar", "Resultado: 6.0"),

    # SUBTRAÇÃO
    ("5", "3", "subtrair", "Resultado: 2.0"),
    ("0", "0", "subtrair", "Resultado: 0.0"),
    ("-1", "-1", "subtrair", "Resultado: 0.0"),
    ("-1", "1", "subtrair", "Resultado: -2.0"),
    ("5.5", "2.2", "subtrair", "Resultado: 3.3"),

    # MULTIPLICAÇÃO
    ("2", "3", "multiplicar", "Resultado: 6.0"),
    ("-1", "1", "multiplicar", "Resultado: -1.0"),
    ("0", "5", "multiplicar", "Resultado: 0.0"),
    ("-1", "-1", "multiplicar", "Resultado: 1.0"),
    ("2.5", "4.0", "multiplicar", "Resultado: 10.0"),

    # DIVISÃO
    ("6", "3", "dividir", "Resultado: 2.0"),
    ("0", "5", "dividir", "Resultado: 0.0"),
    ("-6", "-3", "dividir", "Resultado: 2.0"),
    ("7.5", "2.5", "dividir", "Resultado: 3.0"),

    # DIVISÃO POR ZERO
    ("5", "0", "dividir", "Resultado: Erro: divisao por zero"),
    ("0", "0", "dividir", "Resultado: Erro: divisao por zero"),
]

# Executa cada teste
for a, b, operacao, esperado in casos_de_teste:
    print(f"\n🔢 Testando: {a} {operacao} {b} (esperado: {esperado})")

    # Localiza e limpa os campos
    campo_a = driver.find_element(By.NAME, "a")
    campo_b = driver.find_element(By.NAME, "b")
    campo_a.clear()
    campo_b.clear()
    time.sleep(0.5)

    # Preenche os valores de entrada
    campo_a.send_keys(a)
    time.sleep(0.5)
    campo_b.send_keys(b)
    time.sleep(0.5)

    # Força nova seleção da operação
    select_operacao = Select(driver.find_element(By.NAME, "operacao"))
    select_operacao.select_by_value(operacao)
    time.sleep(1)  # Espera para garantir que a seleção foi aplicada

    # Clica no botão calcular
    botao_calcular = driver.find_element(By.TAG_NAME, "button")
    botao_calcular.click()
    time.sleep(2)

    # Verifica o resultado
    resultado = driver.find_element(By.CLASS_NAME, "resultado").text

    if resultado == esperado:
        print(f"✅ Resultado correto: {resultado}")
    else:
        print(f"❌ Resultado incorreto: {resultado} (esperado: {esperado})")

# Espera para visualização final e fecha navegador
time.sleep(4)
driver.quit()
