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
<<<<<<< HEAD
=======
        #self.usuario.user_permissions.add(Permission.objects.get(codename=''))
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.usuario.set_password('admin')
        self.usuario.save()
        self.client.login(username='admin', password='admin')
        self.ajuste = Ajustes.objects.create()
        
        self.area = Area(
            nombre='Administración',
            siglas='adm'
        )
        
        self.area.save()
        
<<<<<<< HEAD
=======
        
       
        #fields = ('first_name','last_name','username','email','password','area','puesto')
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9

        self.datos = {
            'first_name' : 'Luis',
            'last_name' : 'Limón',
            'username' : 'Llimon',
            'email' : 'tmpcorreotmpnoExiste@gmail.com',
            'password' : '12345678',
            'area' : self.area,
            'puesto' : 'apuesto'
<<<<<<< HEAD
        }
        
    
=======
            #'is_superuser' : True
        }
        
    
        
    
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
    def test_crear_usuario_response(self):
        response = self.client.get('/usuarios/crear/')
        self.assertEqual(response.status_code, 200)
        
<<<<<<< HEAD
   
    
        
    # def test_usuarios_editar_response(self):
    #     self.crear_usuario()
        
    #     self.nuevo_usuario2 = Usuario(
    #         first_name = 'Carlos',
    #         last_name = 'Man',
    #         username = 'Cmadsf2',
    #         email = 'tmpcorreot2mpnoExisteadf2@gmail.com',
    #         password = '12345678',
    #         area = self.area,
    #         puesto = 'apuesto'
    #         #'is_superuser' : True
    #     )
    #     self.nuevo_usuario2.set_password('admin')
    #     self.nuevo_usuario2.save()
    #     response = self.client.get('/usuarios/editar/4')
    #     self.assertEqual(response.status_code, 200)
        
    
        
    def crear_usuario(self):
        self.nuevo_usuario1 = Usuario(
            first_name = 'Carlos',
            last_name = 'Man',
            username = 'Cmadsf',
            email = 'tmpcorreotmpnoExisteadf2@gmail.com',
            password = '12345678',
            area = self.area,
            puesto = 'apuesto'
            #'is_superuser' : True
        )
        self.nuevo_usuario1.set_password('admin')
        self.nuevo_usuario1.save()
        return self.nuevo_usuario1
    
    def test_noagregar_usuario_sin_username(self):
        self.datos['username'] = ''
        self.client.post('/usuarios/crear/', data=self.datos)
        self.assertEqual(Usuario.objects.all().count(), 0)
    
    
    def test_noagregar_usuario_sin_contraseña(self):
        self.datos['password'] = ''
        self.client.post('/usuarios/crear/', data=self.datos)
        self.assertEqual(Usuario.objects.all().count(), 0)
    
    def test_noagregar_usuario_sin_area(self):
        self.datos['area'] = ''
        self.client.post('/usuarios/crear/', data=self.datos)
        self.assertEqual(Usuario.objects.all().count(), 0)
        
    def test_noagregar_usuario_correo_invalido(self):
        self.datos['email'] = 'alksdfj @gmail.com'
        self.client.post('/usuarios/crear/', data=self.datos)
        self.assertEqual(Usuario.objects.all().count(), 0)
        
    def test_noagregar_usuario_username_maxcarcatere(self):
        self.datos['username'] = 'usuario'*30
        self.client.post('/usuarios/crear/', data=self.datos)
        self.assertEqual(Usuario.objects.all().count(), 0)
    
    # def test_crear_ajuste_response(self):
    #     response = self.client.get('/usuarios/ajustes/1')
    #     self.assertEqual(response.status_code, 200)
        
        
   
=======
    def test_template_usuarios_correcto(self):
        response = self.client.get('/usuarios/')
        self.assertTemplateUsed(response, 'usuarios/lista_usuarios.html')
        
            
    def test_usuarios_response(self):
        response = self.client.get('/usuarios/')
        self.assertEqual(response.status_code, 200)
        
    def test_template_crear_usuario_correcto(self):
        response = self.client.get('/usuarios/crear/')
        self.assertTemplateUsed(response, 'usuarios/crear_usuarios.html')
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        
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
    

        