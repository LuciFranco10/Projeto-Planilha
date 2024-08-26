import pandas as pd
from   selenium  import webdriver
from   selenium.webdriver.common.by import By
from   selenium.webdriver.chrome.service import Service
from   webdriver_manager.chrome import ChromeDriverManager
from   selenium.webdriver.support.ui import WebDriverWait
from   selenium.webdriver.support import expected_conditions as EC
from   selenium.webdriver.common.keys import Keys
import time


caminho_planilha = '/home/luciane/projetos/luciane.dev/planilha/projeto_planilha.csv'

colunas = ['Nome', 'Telefone', 'Email']

df = pd.read_csv('projeto_planilha.csv', sep=',' , names=colunas, header=None)

print(df.head())



Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)


url_formulario = 'https://docs.google.com/forms/d/e/1FAIpQLSfkUAzQY8_R46zbw5O98Ni6Gl2Zqq_gdCftgvUWteHilsewNw/viewform'
driver.get(url_formulario)



for index, row in df.iterrows():

    try:

        print(f"Tentando preencher o formulário para o índice {index}")
        
        try:
            nome = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"]'))
            )

        except:
            print("Não foi possível encontrar o campo Nome com o seletor CSS fornecido.")
            driver.save_screenshot(f"erro_indice_{index}_campo_nome.png")
            continue
        
        print("Campo Nome encontrado")
        nome.send_keys(row['Nome'])



        telefone = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[aria-labelledby="i5"]'))
        )
        telefone.send_keys(row['Telefone'])




        email = WebDriverWait(driver, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[aria-labelledby="i2"]'))
        )
        email.send_keys(row['Email'])
         

        # nome.send_keys(row['Nome'])
        # telefone.send_keys(row['Telefone'])
        # email.send_keys(row['Email'])
        # nome_value = nome.get_attribute('value')
        # print(f"Valor do campo nome preenchido para o índice {index}: {nome_value}")


        submit_button = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]'))
       
         )
        submit_button.click()

        time.sleep(2)
    except Exception as e:
          print(f"Erro ao preencher o formulário para o índice {index}: {e}")
          driver.save_screenshot(f"erro_indice_{index}.png")


driver.quit()

