Característica: Agregar Usuario
    Como usuario del sistema
    Quiero entrar al sistema para realizar mis actividaes con los usuarios
    Para tener control de los usuarios que hay.

    Escenario: Poder agregar un usuario
    Dado que ingreso al sistema en el dominio "http://localhost:8000/"
    Y escribo mi usuario "admin" y contraseña "admin"
    Y presiono el boton ingresar
    Y seleciono la pestaña "Usuarios"
    Y seleccionar el boton "Crear usuario"
    Y agrego un nombre "Ramon", un apellido "Ramirez", un nombre de usuario "ramon", pongo el correo "bladimir122020@gmia.com", creo una contraseña "ramon", selecciono una area "Escuela Secundaria" y agrego el pusto que tiene actual "Gefe".
    Cuando  selecciono el boton Agregar
    Entonces vemos que se agrego el usuario "Ramon".