from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




@given(u'seleciono la pestaña "{usuario}"')
def step_impl(context, usuario):
    context.driver.find_element(By.LINK_TEXT, usuario).click()


@given(u'seleccionar el boton "{crear}"')
def step_impl(context, crear):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    time.sleep(3)
    context.driver.find_element(By.LINK_TEXT, crear).click()


@given(u'agrego un nombre "{nombre}", un apellido "{apellido}", un nombre de usuario "{usuario}", pongo el correo "{correo}", creo una contraseña "{contrasena}", selecciono una area "{area}" y agrego el pusto que tiene actual "{puesto}".')
def step_impl(context, nombre, apellido, usuario, correo, contrasena, area, puesto):
    time.sleep(3)
    context.driver.find_element(By.XPATH, '/html/body/aside/div[1]/a').click()
    context.driver.find_element(By.ID, 'id_first_name').send_keys(nombre)
    context.driver.find_element(By.ID, 'id_last_name').send_keys(apellido)
    context.driver.find_element(By.ID, 'id_username').send_keys(usuario)
    context.driver.find_element(By.ID, 'id_email').send_keys(correo)
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasena)
    find_element_area = \
    context.driver.find_element(By.ID, "id_area")
    selec_area_status = Select(find_element_area)
    selec_area_status.select_by_visible_text(area)
    context.driver.find_element(By.ID, 'id_puesto').send_keys(puesto)
    


@when(u'selecciono el boton Agregar')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div/div/form/button").click()

@then(u'vemos que se agrego el usuario "Ramon".')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then vemos que se agrego el usuario "Ramon".')

