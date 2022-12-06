from behave import given, then, when
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys



@given(u'mostramos los detalles la dependencia llamada "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    time.sleep(3)
    tabla = context.driver.find_element(By.TAG_NAME, 'tbody')
    trs = tabla.find_elements(By.TAG_NAME, 'tr')
    print(nombre)
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        if tds[0].text == nombre:
            tds[2].find_element(By.LINK_TEXT, 'Detalles').click()
    time.sleep(3)


@when(u'selecciono el boton "Detalles"')
def step_impl(context):
    pass


@then(u'mostrara los detalles de la dependencia')
def step_impl(context):
    pass