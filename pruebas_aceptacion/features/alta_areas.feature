Característica: Agregar una area
    Como usuario del sistema
    Quiero entrar al sistema para realizar mis actividaes en areas
    Para tener control de las áreas que hay.

    Escenario: Agregar datos correctos
    Dado que ingreso al sistema en el dominio "http://localhost:8000/"
    Y escribo mi usuario "admin" y contraseña "admin"
    Y presiono el boton ingresar
    Y seleciono la pestaña "Administración de areas"
    Y seleciono la opcion "Agregar area"
    Y ingreso el nombre de un area "Area de contaduria" y sus siglas "Ac"
    Cuando presiono el boton "Agregar"
    Entonces puedo ver el elemento "Area de contaduria"
    
    
    Escenario: Agregar area datos incorrectos
    Dado que ingreso al sistema en el dominio "http://localhost:8000/"
    Y escribo mi usuario "admin" y contraseña "admin"
    Y presiono el boton ingresar
    Y seleciono la pestaña "Administración de areas"
    Y seleciono la opcion "Agregar area"
    Y ingreso el nombre mal de un area "Area de administracón" y sus siglas "  "
    Cuando presiono el boton "Agregar"
    Entonces puedo ver el texto "Este campo es obligatorio."

    
    Escenario: Agregar area datos repetidos
    Dado que ingreso al sistema en el dominio "http://localhost:8000/"
    Y escribo mi usuario "admin" y contraseña "admin"
    Y presiono el boton ingresar
    Y seleciono la pestaña "Administración de areas"
    Y seleciono la opcion "Agregar area"
    Y ingreso el nombre de un area "Area 1" y sus siglas "Ac"
    Cuando presiono el boton "Agregar"
    Entonces puedo ver el mensaje "Ya existe un/a Area con este/a Siglas."