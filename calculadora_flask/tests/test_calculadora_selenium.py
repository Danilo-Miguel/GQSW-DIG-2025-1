from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Caminho para o seu chromedriver.exe
caminho_driver = "D:\Documentos\chromedriver-win64\chromedriver-win64/chromedriver.exe"

# Cria o serviço com o caminho
service = Service(caminho_driver)

# Inicia o navegador com o serviço
driver = webdriver.Chrome(service=service)

# Continua normalmente
driver.get("http://127.0.0.1:5000/calculadora")
time.sleep(1)

campo_a = driver.find_element(By.NAME, "a")
campo_b = driver.find_element(By.NAME, "b")
select_operacao = Select(driver.find_element(By.NAME, "operacao"))
botao_calcular = driver.find_element(By.TAG_NAME, "button")

campo_a.send_keys("7")
campo_b.send_keys("3")
select_operacao.select_by_value("somar")
botao_calcular.click()

time.sleep(1)
resultado = driver.find_element(By.CLASS_NAME, "resultado")
print("Resultado exibido:", resultado.text)

driver.quit()
