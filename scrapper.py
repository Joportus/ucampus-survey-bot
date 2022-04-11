from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#  PLEASE dont use this programme if you have covid symptoms or you had close contact with a person with covid!
def ucampus_scrapper(username, password, day="today"):
    """
    Receives username and password for Ucampus, the day when you are going to the university (today or tomorrow) 
    and answers the daily health survey for you
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    ucampus_url = "https://ucampus.uchile.cl/"
    # We connect to the Ucampus website
    driver.get(ucampus_url)
    username_input = driver.find_element_by_name("username")
    username_input.send_keys(username)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)
    submit_button = driver.find_element_by_class_name("boton")
    submit_button.click()
    encuesta_diaria_button = driver.find_element_by_id("fcfm_encuesta_diaria")
    encuesta_diaria_button.click()
    time.sleep(1)
    iframe = driver.find_element_by_id("externo")
    driver.switch_to.frame(iframe)
    if day == "tomorrow":
        fecha_button = driver.find_elements_by_name("encuesta[fecha]")[1]
        fecha_button.click()
    sintomas_check = driver.find_element_by_id("check_sin_sintomas")
    sintomas_check.click()
    time.sleep(1)
    no_contacto_estrecho_button = driver.find_elements_by_name("encuesta[contacto_estrecho]")[1]
    no_contacto_estrecho_button.click()
    submit_button = driver.find_element_by_name("accion")
    submit_button.click()
    time.sleep(5)
    
# Here we call the function, fill in with your credentials
ucampus_scrapper("username", "password", "day(today or tomorrow)")
