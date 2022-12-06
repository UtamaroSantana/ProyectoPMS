from django.test import TestCase
from ficha.forms import DependenciaForm

class TestFormArea(TestCase):
    def setUp(self):
        self.dependencia = {
        'nombre' : 'Zacatecas',
        'siglas' : 'zac'
        }

    def test_dependencia_nombre_con_espacios(self):
        self.dependencia['nombre'] = 'LAEncantada'
        form = DependenciaForm(self.dependencia)
        self.assertTrue(form.is_valid())

    def  test_dependencia_form(self):
        form = DependenciaForm(self.dependencia)
        self.assertFalse(form.is_valid())

    
    def test_dependencia_nombre_vacio(self):
        self.dependencia['nombre'] = ''
        form = DependenciaForm(self.dependencia)
        self.assertFalse(form.is_valid())

    def test_dependencia_siglas_maximo_caracteres(self):
        self.dependencia['nombre'] = 'dfdf'*100
        form = DependenciaForm(self.dependencia)
        self.assertFalse(form.is_valid())

    
    def test_dependencia_siglas_vacio(self):
        self.dependencia['siglas'] = ''
        form = DependenciaForm(self.dependencia)
        self.assertTrue(form.is_valid())


    
    def test_dependencia_siglas_maximo_caracteres(self):
        self.dependencia['siglas'] = 'dfdf'*10
        form = DependenciaForm(self.dependencia)
        self.assertFalse(form.is_valid())