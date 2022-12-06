from behave import given, then, when
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@given(u'que ingreso al sistema en el dominio "{url}"')
def step_impl(context, url):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1300,300")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    context.driver.get(url)


@given(u'escribo mi usuario "{usuario}" y contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(contra)


@given(u'presiono el boton ingresar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '/html/body/div/div/div/div/div/form/div[1]/div[3]/button').click()


@given(u'seleciono la pestaña "Administración de areas"')
def step_impl(context):
    context.driver.find_element(
        By.PARTIAL_LINK_TEXT,
        'Administración de dependencias').click()
    context.driver.find_element(
        By.XPATH, '/html/body/aside/div[2]/div[2]/ul/li[4]/a').click()
    context.driver.maximize_window()


@given(u'seleciono la opcion "Agregar area"')
def step_impl(context):
    context.driver.find_element(
        By.XPATH,
        '/html/body/aside/div[2]/div[2]/ul/li[4]/div/div/ul/li[2]/a').click()


@given(u'ingreso el nombre de un area "{nombre}" y sus siglas "{siglas}"')
def step_impl(context, nombre, siglas):

    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    context.driver.find_element(By.ID, 'id_nombre').send_keys(nombre)
    context.driver.find_element(By.ID, 'id_siglas').send_keys(siglas)


@when(u'presiono el boton "{boton}"')
def step_impl(context, boton):
    context.driver.find_element(
        By.XPATH, '/html/body/main/div/div/form/button').click()


@then(u'puedo ver el elemento "{area}"')
def step_impl(context, area):
    context.driver.refresh()
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    tabla = context.driver.find_element(By.TAG_NAME, 'tbody')
    trs = tabla.find_elements(By.TAG_NAME, 'tr')
    elementos = []

    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        elementos.append(tds[0].text)
    assert area in elementos, str(elementos)


@given(u'ingreso el nombre mal de un area "{nombre}" y sus siglas "  "')
def step_impl(context, nombre):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    context.driver.find_element(By.ID, 'id_nombre').send_keys(nombre)
    context.driver.find_element(By.ID, 'id_siglas').send_keys('  ')


@then(u'puedo ver el texto "{mensaje}"')
def step_impl(context, mensaje):
    context.driver.refresh()
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    time.sleep(3)
    texto = context.driver.find_element(
        By.XPATH, '/html/body/main/div/div/form/ul/li').text
    assert mensaje == texto, texto


@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    context.driver.refresh()
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    time.sleep(3)
    texto = context.driver.find_element(
        By.XPATH, '/html/body/main/div/div/form/ul/li').text
    assert mensaje == texto, texto
