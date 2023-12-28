from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

while True:
    try:
        #Abrir navegador:
        drive = webdriver.Firefox()
        #pesquisar a URL:
        drive.get("https://www.google.com/search?client=firefox-b-d&q=hotmail")
        drive.maximize_window()

        #clicando no primeiro resultado da pesquisa:
        sleep(2)
        drive.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
        #clicando em login dentro da pagina:
        sleep(2)
        drive.find_element(By.XPATH, '/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
        #selecionando campo de e-mail e digidando informação:
        sleep(2)
        drive.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('carlo.henrique37@hotmail.com')
        drive.find_element(By.ID, 'idSIButton9').click()
        #selecionando campo de senha e digitando informação:
        sleep(2)
        drive.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('54544761Chpj')
        drive.find_element(By.ID, 'idSIButton9').click()
        #clicando em "Não" para pergunta de "Continuar conectado?":
        sleep(3)
        drive.find_element(By.ID, 'idBtn_Back').click()
        #clicando em novo e-mail:
        sleep(1)
        drive.find_element(By.ID, 'id__135').click()
        #clicando no campo de"Para" e digitando e-mail de destinatario:
        sleep(2)
        drive.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[1]/div/div[3]/div/div/div[2]').send_keys('Anacarolinareis1211@hotmail.com')
        #clicando no campo de "assunto" e digitando informação:
        sleep(2)
        drive.find_element(By.XPATH, '//*[@id="TextField239"]').send_keys('AutomacaoBotEmail')
        #clicando no campo de "Corpo do e-mail" e digitando o e-mail que sera enviado:
        sleep(1)
        drive.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div[3]/div[3]/div[1]/div/div/div/div[4]/div/div[1]/div').send_keys('TE AMO MIL MILHÕES S2')
        #clicando no botão de envio e enviando e-mail:
        #sleep(2)
        #drive.find_element(By.ID, 'id__221').click()
        break

    #Quando é encontrado uma exceção entra aqui:
    except:
        #Abre uma caixa de mensagem com uma pergunta, "Quer reiniciar o programa?":
        #Se a reposta for "sim" o programa voltara ao inicio do laço de repetição:
        if messagebox.askyesno(title='ATENÇÃO: Houve um erro', message='Quer reiniciar o programa?') == True:
            continue
        #Se a resposta for "não" o programa vai se encerrar:
        else:   
            break
#Notificação de encerramento do programa:
messagebox.showinfo(title='ATENÇÃO', message='O PROGRAMA PAROU')
