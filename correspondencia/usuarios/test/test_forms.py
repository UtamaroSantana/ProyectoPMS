# Create your tests here.
from django.test import TestCase
<<<<<<< HEAD
from usuarios.forms import UsuarioForm, AjustesForm
=======
from usuarios.forms import UsuarioForm
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
from django.contrib.auth.models import User
from ficha.models import Area
from ficha.forms import AreaForm
from usuarios.models import Ajustes
from usuarios.models import Usuario


# Create your tests here.
# 'first_name','last_name','username','email','password','area','puesto'

class TestFormUser(TestCase):
    
    def setUp(self, nombre = "Juan", apellido="Socorro",userna='jsoco',correo='juan32350@gmail.com', puestoT='apuesto', passwd='12344798123749812734'):
        
        
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
            'first_name' : nombre,
            'last_name' : apellido,
            'username' : userna,
            'email' : correo,
            'password' : passwd,
            'area' : self.area,
            'puesto' : puestoT
            #'is_superuser' : True
        }
        
<<<<<<< HEAD
        self.datosAjuste = {
            'titulo' : 'titulo de prueba',
            'subtitulo' : 'sub titulo'
        }
        
   
=======
        # self.datos = {
        #     'username' : nombre,
        #     'email' : correo,
        #     'password' : passwd,
        #     'is_superuser' : True
        # }
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        
    def test_usuario_form_valido(self):
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())

<<<<<<< HEAD
    def test_ajuste_form_valido(self):
        form = AjustesForm(self.datosAjuste)
        self.assertTrue(form.is_valid())
        
    def test_usuario_form_contraseña_vacia_invalida(self):
=======
        
        
    def test_usuario_form_contraseña_vacia(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['password'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
    
<<<<<<< HEAD
    def test_usuario_form_apellido_maxcarctere_invalido(self):
=======
    def test_usuario_form_apellido_maxcarctere(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['last_name'] = 'a'*200
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
<<<<<<< HEAD
    def test_usuario_form_apellido_maxcarcteres150_valido(self):
=======
    def test_usuario_form_apellido_maxcarcteres150(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['last_name'] = 'a'*150
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())
        
<<<<<<< HEAD
    def test_usuario_form_nombre_maxcarctere_invalido(self):
=======
    def test_usuario_form_nombre_maxcarctere(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['first_name'] = 'a'*200
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
<<<<<<< HEAD
    def test_usuario_form_nombre_maxcarcteres150_valido(self):
=======
    def test_usuario_form_nombre_maxcarcteres150(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['first_name'] = 'a'*150
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())
        
         
<<<<<<< HEAD
    def test_usuario_form_correo_maxcarctere_invalido(self):
=======
    def test_usuario_form_correo_maxcarctere(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['email'] = 'a'*255
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
    def test_usuario_form_correo_formato_invalido(self):
        self.datos['email'] = 'juan3235 0@gmail.com'
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
<<<<<<< HEAD

    def test_usuario_form_area_vacio_invalido(self):
=======
    # def test_usuario_form_email_vacio(self):
    #     self.datos['email'] = ''
    #     form = UsuarioForm(self.datos)
    #     self.assertFalse(form.is_valid())
    
    # def test_usuario_form_apellido_vacio(self):
    #     self.datos['last_name'] = ''
    #     form = UsuarioForm(self.datos)
    #     self.assertFalse(form.is_valid())
    
    # def test_usuario_form_nombre_vacio(self):
    #     self.datos['first_name'] = ''
    #     form = UsuarioForm(self.datos)
    #     self.assertFalse(form.is_valid())

    def test_usuario_form_email_vacio(self):
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
        self.datos['area'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
<<<<<<< HEAD
    def test_usuario_form_puesto_vacio_invalido(self):
        self.datos['puesto'] = ''
        form = UsuarioForm(self.datos)
        self.assertFalse(form.is_valid())
        
    def test_usuario_form_email_no_requerido(self):
        self.datos['email'] = ''
        form = UsuarioForm(self.datos)
        self.assertTrue(form.is_valid())
        
    def test_ajuste_form_titulo_maxcaracteres_invalido(self):
        self.datosAjuste['titulo'] = 'titulo'*30
        form = AjustesForm(self.datosAjuste)
        self.assertFalse(form.is_valid())
    
    def test_ajuste_form_subtitulo_maxcaracteres_invalido(self):
        self.datosAjuste['subtitulo'] = 'subtitulo'*30
        form = AjustesForm(self.datosAjuste)
        self.assertFalse(form.is_valid())
   
    def test_ajuste_form_subtitulo_espacios_invalido(self):
        self.datosAjuste['subtitulo'] = 'subtitulo'
        form = AjustesForm(self.datosAjuste)
        self.assertFalse(form.is_valid())
=======
>>>>>>> dc3e884189f000893ad19044488c2c51da46ebd9
    
        
    
        
    
    
    
