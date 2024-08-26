import pandas as pd
from   selenium  import webdriver
from   selenium.webdriver.common.by import By
from   selenium.webdriver.chrome.service import Service
from   webdriver_manager.chrome import ChromeDriverManager
from   selenium.webdriver.common.keys import Keys
import time


caminho_planilha = '/home/luciane/projetos/luciane.dev/planilha/projeto_planilha.xlsx'

df = pd.read_excel(caminho_planilha)

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)


url_formulario = 'https://docs.google.com/forms/d/e/1FAIpQLSfkUAzQY8_R46zbw5O98Ni6Gl2Zqq_gdCftgvUWteHilsewNw/viewform'
driver.get(url_formulario)


for index, row in df.iterrows():

    try:


        nome = driver.find_element(By.NAME, 'nome')
        telefone = driver.find_element(By.NAME,'telefone')
        email = driver.find_element(By.NAME, 'email')

        nome.send_keys(row['Nome'])
        telefone.send_keys(row['Telefone'])
        email.send_keys(row['Email'])


        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]'))
        
        )
        
        submit_button.click()

        time.sleep(2)
    except Exception as e:
         print(f"Erro ao preencher o formulário para o índice {index}: {e}")


driver.quit()