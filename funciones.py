import usuario,administrador

def login():
    print("-----Login------")
    us=input("Ingrese usuario: ")
    password=input("Ingrese contraseña: ")
    while True:
        if administrador.admin0(us,password):
            print("--Acceso ADMIN concedido--")
            administrador.menu_adminitrador()
        elif usuario.user0(us,password):
            print("--Acceso User concedido--")
            usuario.menu_usuario()
        else:
            print("--Acceso denegado--")
            break

def mostrar_usuarios():
    print("----Usuarios Registrados----")
    lista=ver_usuario()
    if len(lista)==0:
        print("No hay usuarios registrados")
        return
    for u in lista:
        print("---------------------")
        print(
            f"ID: {u['id']} |"
            f"Usuario: {u['usuario']}"
        )
        print("---------------------")


Usuarios= [
    {
        "id":1,
        "usuario":"user",
        "contraseña":"12345"
    }
]

    
def registrar_usuario(usuario,contraseña):
    for u in Usuarios:
        if u["usuario"]==usuario:
            return False
    
    nuevo_id=max(u["id"] for u in Usuarios)+1

    nuevo_usuario={
        "id":nuevo_id,
        "usuario":usuario,
        "contraseña":contraseña
    }
    Usuarios.append(nuevo_usuario)
    return True

def ver_usuario():

    return Usuarios

def eliminar_usuario():
    Usuarios=()