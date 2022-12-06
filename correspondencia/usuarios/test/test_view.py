from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from usuarios.models import Ajustes, Usuario
from ficha.models import Area
from usuarios.forms import UsuarioForm



class TestViewsUsuario(TestCase):
    def setUp(self):
        self.usuario = User(
             username='admin',
             email='',
             password='admin',
             is_superuser=True,
             is_active=True
        )
        #self.usuario.user_permissions.add(Permission.objects.get(codename=''))
        self.usuario.set_password('admin')
        self.usuario.save()
        self.client.login(username='admin', password='admin')
        self.ajuste = Ajustes.objects.create()
        
        self.area = Area(
            nombre='Administración',
            siglas='adm'
        )
        
        self.area.save()
        
        
       
        #fields = ('first_name','last_name','username','email','password','area','puesto')

        self.datos = {
            'first_name' : 'Luis',
            'last_name' : 'Limón',
            'username' : 'Llimon',
            'email' : 'tmpcorreotmpnoExiste@gmail.com',
            'password' : '12345678',
            'area' : self.area,
            'puesto' : 'apuesto'
            #'is_superuser' : True
        }
        
    
        
    
    def test_crear_usuario_response(self):
        response = self.client.get('/usuarios/crear/')
        self.assertEqual(response.status_code, 200)
        
    def test_template_usuarios_correcto(self):
        response = self.client.get('/usuarios/')
        self.assertTemplateUsed(response, 'usuarios/lista_usuarios.html')
        
            
    def test_usuarios_response(self):
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 200)
        
    def test_template_crear_usuario_correcto(self):
        response = self.client.get('/usuarios/crear/')
        self.assertTemplateUsed(response, 'usuarios/crear_usuarios.html')
        
    def test_agregar_usuario_valido(self):
        area1 = Area(
            nombre='Contaduria',
            siglas='cn'
        )
        
        area1.save()
        nuevo_usuario1 = {
            'first_name' : 'Carlos',
            'last_name' : 'Man',
            'username' : 'Cm',
            'email' : 'tmpcorreotmpnoExiste2@gmail.com',
            'password' : '12345678',
            'area' : area1,
            'puesto' : 'apuesto'
            #'is_active': True
            #'is_superuser' : True
        }
        # nuevo_usuario1 = Usuario(
        #     first_name = 'Carlos',
        #     last_name = 'Man',
        #     username = 'Cm',
        #     email = 'tmpcorreotmpnoExiste2@gmail.com',
        #     password = '12345678',
        #     area = area1,
        #     puesto = 'apuesto'
        #     #'is_superuser' : True
        # )
        #nuevo_usuario1.set_password('admin')
        #nuevo_usuario1.save()
        #form = UsuarioForm(nuevo_usuario1)
        #self.assertTrue(form.is_valid())
        #self.assertEqual(Area.objects.all().count(), 1)  
        self.client.post('/usuarios/crear/', data=nuevo_usuario1)
        #self.client.get('/usuarios/crear/', data=nuevo_usuario1)
        self.assertEqual(Usuario.objects.all().count(), 0)  
    

        