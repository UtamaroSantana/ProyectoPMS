from django.test import TestCase
from ficha.models import Dependencia
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self, nombre='admin', password='admin'):
        self.dependencia = Dependencia(
            nombre='Administración',
            siglas='adm'
        )

    def test_nombre_es_requerido(self):
        dependencia = Dependencia(
            siglas= 'ert'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_siglas_es_requerido(self):
        dependencia = Dependencia(
            nombre= 'Encantadeitor'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_siglas_y_nombre_es_requerido(self):
        dependencia = Dependencia(
            
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_nombre_menor_201(self):
        dependencia = Dependencia(
            nombre= 'f'*201,
            siglas = 'fff'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_nombre_mayor_4(self):
        dependencia = Dependencia(
            nombre= 'fff',
            siglas = 'fff'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()
    
    def test_nombres_no_acepta_caracteres_especiales(self):
        dependencia = Dependencia(
            nombre= 'ffdd@',
            siglas = 'fdd'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_nombre_no_acepta_cadena_espacios(self):
        dependencia = Dependencia(
            nombre= '     ',
            siglas = 'eee'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_siglas_menor_21(self):
        dependencia = Dependencia(
            nombre= 'fffff',
            siglas = 'f'*21
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    def test_siglas_mayor_2(self):
        dependencia = Dependencia(
            nombre= 'ffffff',
            siglas = 'f'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()
    
    def test_siglas_no_acepta_caracteres_especiales(self):
        dependencia = Dependencia(
            nombre= 'ffddff',
            siglas = 'fdd@'
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()


    def test_siglas_no_acepta_cadena_espacios(self):
        dependencia = Dependencia(
            nombre= 'ffddff',
            siglas = '  '
        )
        with self.assertRaises(ValidationError):
            dependencia.full_clean()

    # def test_usuario_form_nombre_vacio(self):
    #     self.datosUsuario.first_name = ''
    #     form = UsuarioForm(self.datosUsuario)

    # def test_return_object_usuario(self):
    #     self.usuario.full_clean()
    #     self.usuario.save()
    #     self.assertEqual(User.objects.first().username, self.usuario.__str__())