from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Firefox()

navegador.get("https://www.google.com/")

navegador.maximize_window()

sleep(3)

navegador.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Olá')
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
