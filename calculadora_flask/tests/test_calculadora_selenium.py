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

campo_a = driver.find_element(By.NAME, "a")
campo_b = driver.find_element(By.NAME, "b")
select_operacao = Select(driver.find_element(By.NAME, "operacao"))
botao_calcular = driver.find_element(By.TAG_NAME, "button")
time.sleep(2)  # Espera a página carregar

campo_a.send_keys("7")
campo_b.send_keys("3")
select_operacao.select_by_value("somar")
botao_calcular.click()
time.sleep(2)  # Espera o resultado ser calculado

resultado = driver.find_element(By.CLASS_NAME, "resultado")
print("Resultado da soma:", resultado.text)

driver.quit()  # Fecha o navegador após o teste
