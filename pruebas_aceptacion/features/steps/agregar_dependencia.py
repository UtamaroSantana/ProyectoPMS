from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


@given(u'seleciono la pestaña "Administración de dependencias"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[2]/div[2]/ul/li[5]/a').click()


@given(u'seleciono la opcion "Agregar dependencia"')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/aside/div[2]/div[2]/ul/li[5]/div/div/ul/li[2]/a').click()


@when(u'ingreso el nombre de una dependencia "{nombre}" y sus siglas "{siglas}"')
def step_impl(context, nombre, siglas):
    context.driver.find_element(By.ID, 'id_nombre').send_keys(nombre)
    context.driver.find_element(By.ID, 'id_siglas').send_keys(siglas + Keys.ENTER)
