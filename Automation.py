from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By



# Incializando o navegador que será executado todo o script
driver = webdriver.Chrome()

# Abre o Linkeding 
driver.get("https://www.linkedin.com/")

# Definindo os usuários do linkeding
# Lembre-se que é necessário gerar um token para não deixar o usuário em código puro
Email = "diassilveira7@gmail.com"
Senha = "asd4250"

# Encontre o campo de email e preencha com o seu email
users = driver.find_element(By.ID, "session_key").send_keys(Email)

# Encontre o campo de senha e preencha com a sua senha
users_Key = driver.find_element(By.ID, "session_password").send_keys(Senha)

# Encontre o botão 
btn = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")

# Da um tempo para carregar, caso o botão demore para aparecer na tela
time.sleep(3)
# Aqui é onde está ocorrendo a ação de click no botão de entrar 
btn.click()

# Aguardando o carregamento da página após realizar o login
time.sleep(6)

# Procurado o Elemento de Busca no Arquivo HTML
Element_Input = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
# Aguardando encontrar o ELemento
time.sleep(3)

# Realiza o click na Barra de Busca
Element_Input.click()

# Agora você pode digitar um tema para buscar
tema = "Segurança da informação"
Element_Input.send_keys(tema)

# Pressione Enter para realizar a busca
Element_Input.send_keys(Keys.ENTER)

# Tempo apenas para carregar os usuários com tema PROGRAMADOR
time.sleep(4)

# Localizando o Button "Pessoas"
btn_Pessoas = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[2]/button")
# Tempo de espera para que carregue totalmente a página
time.sleep(5)
# Realiza a ação de click no botão de "Pessoas"
btn_Pessoas.click()

# Tempo de carregamento da página até mostrar toda a lista de pessoas
time.sleep(4)


Quantidade_Pessoas = 4

for i in range(Quantidade_Pessoas):
    
    # Localizando o elemento Button "Connect" para cada pessoa
    xpath_connect = f"/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{ i + 1}]/div/div/div/div[3]/div/button/span"

    if i + 1 == 3:
        continue

    time.sleep(3)
    btn_connect = driver.find_element(By.XPATH, xpath_connect)

    # Tempo de espera para que carregue totalmente a página
    time.sleep(3)
    # Realiza a ação de click no botão de "Connect"
    btn_connect.click()

    # Tempo de espera após seguir uma pessoa
    time.sleep(2)

    # Aqui é onde realiza a procura do elemento Button para não enviar nenhuma nota ao realizar a conexão com o usuário
    btn_notas = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span  ")
    # Esperando um tempo para que possa encontrar o botão
    time.sleep(2)
    # Realiza o click no Button após carregar toda a página
    btn_notas.click()
    time.sleep(3)

input("Pressione enter para encerrar")
