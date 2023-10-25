#Importação das bibliotecas
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1 #Pausa em cada comando do pyautogui

#1. Abrindo o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)#Aguardando
pyautogui.press("enter")
time.sleep(10)#Aguardando

#2. Digitando o site que queremos entrar na barra de navegação 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(4)# Aguardando a digitação correta
pyautogui.press("enter")

time.sleep(8) # Esperando o site carregar

#3. Clicando no campo email
pyautogui.click(x=1696, y=386)

#4. Digitando o email
pyautogui.write("email_teste_gabriel@outlook.com")
time.sleep(2) #Aguardando

#5. Mudando de Campo
pyautogui.press("tab")

#6. Digitando a Senha
pyautogui.write("123456")

#7. Clicando no botão de entrar no sistema
pyautogui.click(x=1850, y=559)


# 8. Importação da base de dados. 
tabela = pd.read_csv("produtos.csv")


#9. Cadastro dos produtos. Como iremos cadastrar uma base de dados inteira, colocamos essa ação dentro de um,
#Loop de repetição, para cadastrar todos os nossos produtos.

'''Tabela.index retorna o indice da linha da base de dados
   Então para cada linha dentro da nossa tabela, temos um índice associada a ela e utilizamos isso para encontrar,
   o valor que estamos buscando.
   for linha in tabela.index:'''

    #Clicando no primeiro campo - código
    pyautogui.click(x=1756, y=264)


    # Cadastrando produtos

    ''' Utilizamos o método "loc" da nossa tabela que é um DataFrame do pandas, para localizarmos dentro da,
    nossa base de dados o valor exato que iremos cadastrar no campo.
    Nesse método, passamos a linha(index) e a coluna que esta aquela informação.'''

    #Preenchendo o campo "Código"
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Preenchendo o campo "Marca"
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Preenchendo o campo "tipo"
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Preenchendo o campo "categoria"
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Preenchendo o campo "preco_unitario"
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Preenchendo o campo "custo"
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    #Mudando de campo
    pyautogui.press("tab")

    #Criando a variável obs
    obs = (tabela.loc[linha,"obs"])

    # Se o valor da coluna "obs" não é nulo, então escreva, caso contrário pressione a tecla "tab" e segue o
    # o código.
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")

    # Finaliza o cadastro do produto, pressionando a tecla "enter". Uma vez que o botão enviar, fica selecionado.
    pyautogui.press("enter")
    time.sleep(2)

    # Dar um scroll de tudo para cima para continuar cadastrando os produtos
    pyautogui.scroll(5000)


