from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group
from usuarios.models import Ajustes
from ficha.models import Area


class TestViews(TestCase):
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
        
        self.datos_area = {
            'nombre':'area1',
            'siglas':'a1'
        }

        
    
    def teset_agregar_area(self):
        self.nueva_area = {
            'nombre':'nueva',
            'siglas':'nv'
        }
        self.client.post('/areas/crear/', data=self.nueva_area)
        self.assertEqual(Area.objects.all().count(), 1)  
    
    
    def test_no_agrega_area_nombre_vacio(self):
        self.datos_area['nombre'] = ''
        self.client.post('/areas/crear/', data=self.datos_area)
        self.assertEqual(Area.objects.all().count(), 0)    
        
    
    def test_no_agrega_area_siglas_vacio(self):
        self.datos_area['siglas'] = ''
        self.client.post('/areas/crear/', data=self.datos_area)
        self.assertEqual(Area.objects.all().count(), 0)  
        
         
        
    def test_areas_crear(self):
        response = self.client.get('/areas/crear/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_login(self):
         response = self.client.get('/login/')
         self.assertEqual(response.status_code, 200)

    def test_login_bucar_titulo(self):
         response = self.client.get('/login/')
         titulo = '<title>Inicio de sesión</title>'
         self.assertInHTML(titulo, response.rendered_content)
    
    
        
    
    def test_crear_area_buscar_titulo(self):
         response = self.client.get('/areas/')
         titulo = '<title> Listado de areas </title>'
         self.assertInHTML(titulo, response.rendered_content)
         
        
        

    # def asigna_permisos_login(self):
    #     user1 = User.objects.create_user(
    #         username='admin',
    #         password='admin',
    #         email='',
    #         is_active=True
    #     )
    #     self.client.login(username='admin', password='admin')