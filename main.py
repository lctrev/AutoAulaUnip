import selenium
import time
from selenium import webdriver

def login():
    user = ""
    password = ""
    driver.find_element_by_id("inputRA").send_keys(user)
    driver.find_element_by_id("inputSenha").send_keys(password)
    driver.find_element_by_class_name("btn-lg").click()
    
driver = webdriver.Firefox()
driver.get("https://www.unip.br/aluno/central/")
login()
time.sleep(2)
driver.get("https://www.unip.br/aluno/central/sistemas/acesso/258")
time.sleep(2)
driver.find_element_by_id("linkAul").click()
time.sleep(3)
driver.switch_to.alert.accept()
