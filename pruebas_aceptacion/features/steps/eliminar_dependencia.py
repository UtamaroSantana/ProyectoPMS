from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# @given(u'que ingreso al sistema en el dominio "{url}"')
# def step_impl(context, url):
#     context.driver = webdriver.Firefox()
#     context.driver.get(url)

# @given(u'escribo mi usuario "{usuario}" y contraseña "{contra}"')
# def step_impl(context, usuario, contra):
#     context.driver.find_element(By.NAME, 'username').send_keys(usuario)
#     context.driver.find_element(By.NAME, 'password').send_keys(contra)

# @when(u'presiono el boton ingresar')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/div[1]/div[3]/button').click()


@given(u'seleciono la opcion "Mostrar dependencias"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[2]/div[2]/ul/li[5]/div/div/ul/li[1]/a').click()


@given(u'eliminamos la depandencia "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    time.sleep(3)
    tabla = context.driver.find_element(By.TAG_NAME, 'tbody')
    trs = tabla.find_elements(By.TAG_NAME, 'tr')
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        print(tds[0].text)
        if tds[0].text == nombre:
            tds[2].find_element(By.CLASS_NAME, 'btn-danger').click()
    time.sleep(3)
    #context.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/form/button').click()
    # context.driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/table/tbody/tr[3]/td[3]/button').click()
    # WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[1]/table/tbody/tr[3]/td[3]/button"))).click()

@then(u'confirmamo la eliminacion de la dependencia "Sí, si quiero"')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/form/button').click()

# tabla = context.driver.find_element(By.TAG_NAME, 'tbody')
#     trs = tabla.find_elements(By.TAG_NAME, 'tr')
#     articulos = []
#     for tr in trs:
#         tds = tr.find_elements(By.TAG_NAME, 'td')
#         articulos.append(tds[0].text)
