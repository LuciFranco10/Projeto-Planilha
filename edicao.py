import pandas 
from   selenium  import webdriver
from   selenium.webdriver.common.by import By
from   selenium.webdriver.chrome.service import Service
from   webdriver_manager.chrome import ChromeDriverManager
from   selenium.webdriver.support.ui import WebDriverWait
from   selenium.webdriver.support import expected_conditions as EC
from   selenium.webdriver.common.keys import Keys
import time


excel_data_df = pandas.read_excel('projeto_planilha.xlsx')
print('Mostrar todos os dados da planilha')
print(excel_data_df)

print('\n\n')

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

url_formulario = 'https://docs.google.com/forms/d/e/1FAIpQLSfkUAzQY8_R46zbw5O98Ni6Gl2Zqq_gdCftgvUWteHilsewNw/viewform'
driver.get(url_formulario)
time.sleep(5)


      
for index, row in excel_data_df.iterrows():
    

    try:
        print(f"Tentando preencher o formulário para o índice {index}")

        # Verificar valor da célula
        nome_value = row['Nome'].strip()  # Remove espaços extras
        print(f"Valor para o campo Nome: '{nome_value}'")
       
        # Localizar e preencher o campo Nome
        try:
            nome = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[jsname="YPqjbf"]'))
            )
            print("Campo Nome encontrado com CSS Selector")
            
            # Verifique se o campo está visível e tente preencher
            if  nome.is_displayed():
                nome.clear()  # Limpa o campo antes de preencher
                nome.send_keys(nome_value)
                print(f"Nome '{nome_value}' enviado com sucesso.")
            else:
                raise Exception("Campo Nome não está visível.")
        
        except Exception as e:
            print(f"Não foi possível encontrar ou preencher o campo Nome para o índice {index}: {e}")
            driver.save_screenshot(f"erro_indice_{index}_campo_nome.png")
            continue

       
        print('\n\n')
        

        # Verificar valor da célula do telefone
        tel_value = str(row['Telefone']).strip()  # Remove espaços extras
        print(f"Valor para o campo Telefone: '{tel_value}'")

        try:
            telefone = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@jsname="YPqjbf" and @aria-labelledby="i1"]'))
            )
            print("Campo Telefone encontrado com CSS Selector")

            if  telefone.is_displayed():
                telefone.clear()  # Limpa o campo antes de preencher
                telefone.send_keys(tel_value)
                print(f"Telefone '{tel_value}' enviado com sucesso.")
            else:
                raise Exception("Campo Telefone não está visível.")
        
        except Exception as e:
            print(f"Não foi possível encontrar ou preencher o campo Telefone para o índice {index}: {e}")
            driver.save_screenshot(f"erro_indice_{index}telefone.png")
            continue


    #     # Localizar e clicar no botão de envio
    #     try:
    #         submit_button = WebDriverWait(driver, 30).until(
    #             EC.element_to_be_clickable((By.XPATH, '//span[text()="Enviar"]'))  # Ajuste o seletor conforme necessário
    #         )
    #         submit_button.click()
    #         print("Botão Enviar clicado")
    #     except Exception as e:
    #         print(f"Não foi possível encontrar ou clicar no botão de envio para o índice {index}: {e}")
    #         driver.save_screenshot(f"erro_indice_{index}_botao_envio.png")
    #         continue

    #     # Esperar um pouco para garantir que o envio seja processado
    #     time.sleep(2)

    except Exception as e:
        print(f"Erro ao preencher o formulário para o índice {index}: {e}")
    driver.save_screenshot(f"erro_indice_{index}.png")