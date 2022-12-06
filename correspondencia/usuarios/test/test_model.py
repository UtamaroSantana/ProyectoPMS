from django.test import TestCase
from django.core.exceptions import ValidationError
from ficha.models import Area
from usuarios.forms import UsuarioForm
from django.contrib.auth.models import User
from usuarios.models import Ajustes
from usuarios.models import Usuario


class TestModels(TestCase):
    def setUp(self):
        self.area = Area(
            nombre = 'Contaduria',
            siglas = 'Cta'
        )
        self.area.save()

            
            
          
    
    def test_agreagar_usuario_valido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'Cm',
            email = 'tmpcorreotmpnoExiste2@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        usuario1.set_password('admin')
        usuario1.save()
        self.assertEqual(Usuario.objects.first().last_name + ' '+ Usuario.objects.first().first_name, usuario1.__str__())

        
        
    def test_usuario_username_es_requerido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = '',
            email = 'tmpcorreotmpnoExiste2@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
    
  
            
    def test_usuario_correo_invalido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'hola',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
    
    def test_usuario_correo_invalido_espacios(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'hola123@ .com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
             
    def test_usuario_correo_es_requerido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = ' ',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
    
    def test_usuario_nombre_invalido_max_caracteres(self):
        usuario1 = Usuario(
            first_name = 'Carlos'*200,
            last_name = 'Man',
            username = 'cman',
            email = 'correo@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
            
    def test_usuario_apellido_invalido_max_caracteres(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man'*200,
            username = 'cman',
            email = 'correo@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
               
    def test_usuario_contr_es_requerido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'correo@gmail.com',
            password = '',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
            
    def test_usuario_area_es_requerido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'correo@gmail.com',
            password = 'alksdjfasdf',
            area = None,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()

    def test_usuario_puesto_es_requerido(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'correo@gmail.com',
            password = 'alksdjfasdf',
            area = self.area,
            puesto = ''
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
    
    def test_usuario_username_invalido_max_caracteres(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman'*200,
            email = 'correo@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
            
    def test_usuario_correo_invalido_max_caracteres(self):
        usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'cman',
            email = 'correo@gmail.com'*200,
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        with self.assertRaises(ValidationError):
            usuario1.full_clean()
    