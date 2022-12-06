# from django.test import TestCase

# class TestViews(TestCase):

#     def test_url_dependencia_agregar(self):
#         response = self.client.get('dependencias/crear')

#         self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from ficha.models import Dependencia
from usuarios.models import Ajustes


class TestView(TestCase):
    def setUp(self):
        usuario = User(
            username='admin',
            is_superuser=True,
            
        )
        usuario.set_password('admin')
        usuario.save()
        self.client.login(username='admin', password='admin')
        #self.client.force_login(usuario) 

        self.ajuste = Ajustes.objects.create()

        self.dependencia = {
            'nombre' : 'Chicago',
            'siglas' : 'cc'
        }
        # dependencia = Dependencia(
        #     nombre='Chicago',
        #     siglas='cc'
        # )


    # def asigna_permisos_login(self):
    #     usuario = User.objects.create_user(
    #         username='admin',
    #         password='admin'
    #     )
        
    #     usuario.permissions.add(Permission.objects.get(codename='ficha.view_dependencia'))
    #     self.client.login(username='admin', password='admin')
        
        
    def test_lista_dependencia_estatus(self):
        respuesta = self.client.get('/dependencias/')
        self.assertEquals(respuesta.status_code, 200)
        
        
    def test_formulario_dependencia_nuevo(self):        
        respuesta = self.client.get('/dependencias/crear/')
        self.assertEquals(respuesta.status_code, 200)
        
        
    # def test_template_dependencia_nuevo(self):
    #     response = self.client.get('/dependencias/')
    #     self.assertTemplateUsed(response, 'crear')

    def test_no_agrega_con_nombre_max_caracteres(self):
        self.dependencia['nombre'] = 'jorge'*50
        self.client.post('/dependencias/crear/', data=self.dependencia)
        self.assertEqual(Dependencia.objects.all().count(), 0)

    def test_no_agrega_con_nombre_con_espacios(self):
        self.dependencia['nombre'] = 'jorge alfonso'
        self.client.post('/dependenca/crear', data=self.dependencia)
        self.assertEqual(Dependencia.objects.all().count(), 0)
    