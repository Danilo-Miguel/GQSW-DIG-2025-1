from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

#caminho do chromedriver
CHROMEDRIVER_PATH ="D:\Documentos\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Configuração do serviço do ChromeDriver
service = Service(CHROMEDRIVER_PATH)

# Inicialização do WebDriver
driver = webdriver.Chrome(service=service)

# Acessar a página da calculadora
driver.get("http://127.0.0.1:5000/calculadora")
time.sleep(2)  # Espera a página carregar

# Lista de casos de teste

casos_de_teste = [
    #SOMA
    ("2", "3", "somar", "Resultado:5.0"),
    ("-1", "1", "somar", "Resultado:0.0"),
    ("0", "0", "somar", "Resultado:0.0"),
    ("-1", "-1", "somar", "Resultado:-2.0"),
    ("2.5", "3.5", "somar", "Resultado:6.0"),

    #SUBTRAÇÃO
    ("5", "3", "subtrair", "Resultado:2.0"),
    ("0", "0", "subtrair", "Resultado:0.0"),
    ("-1", "-1", "subtrair", "Resultado:0.0"),
    ("-1", "1", "subtrair", "Resultado:-2.0"),
    ("5.5", "2.2", "subtrair", "Resultado:3.3"),

    #MULTIPLICAÇÃO
    ("2", "3", "multiplicar", "Resultado:6.0"),
    ("-1", "1", "multiplicar", "Resultado:-1.0"),
    ("0", "5", "multiplicar", "Resultado:0.0"),
    ("-1", "-1", "multiplicar", "Resultado:1.0"),
    ("2.5", "4.0", "multiplicar", "Resultado:10.0"),

    #DIVISÃO
    ("6", "3", "dividir", "Resultado:2.0"),
    ("0", "5", "dividir", "Resultado:0.0"),
    ("-6", "-3", "dividir", "Resultado:2.0"),
    ("7.5", "2.5", "dividir", "Resultado:3.0"),

    #DIVISÃO POR ZERO
    ("5", "0", "dividir", "Erro: divisao por zero"),
    ("0", "0", "dividir", "Erro: divisao por zero"),
    
]  


for a, b, operacao, resultado_esperado in casos_de_teste:
    print(f"Testando: {a} {operacao} {b} (esperado: {resultado_esperado})")

    # Localiza os campos de entrada e o botão
    campo_a = driver.find_element(By.NAME, "a")
    campo_b = driver.find_element(By.NAME, "b")
    campo_a.clear()  # Limpa o campo antes de enviar os dados
    campo_b.clear()  # Limpa o campo antes de enviar os dados   
    time.sleep(0.5)  # Espera um segundo para garantir que os campos estejam prontos


    campo_a.send_keys(a)
    time.sleep(1)  # Espera um segundo para garantir que o campo esteja pronto
    campo_b.send_keys(b)
    time.sleep(1)  # Espera um segundo para garantir que o campo esteja pronto

    select_operacao = Select(driver.find_element(By.NAME, "operacao"))
    select_operacao.select_by_value(operacao)
    time.sleep(1)  # Espera um segundo para garantir que a operação esteja selecionada

    botao_calcular = driver.find_element(By.TAG_NAME, "button")
    botao_calcular.click()
    time.sleep(2)  # Espera a página carregar


    resultado = driver.find_element(By.CLASS_NAME, "resultado")

    if resultado.text != resultado_esperado:
        print(f"Resultado correto {resultado_esperado}")
    else:
        print(f"Resultado incorreto: {resultado.text}")
    
time.sleep(2)
driver.quit()  # Fecha o navegador após o teste
