def iniciar_sesion(usuario, contraseña, usuarios, administradores):
    for admin in administradores:
        if usuario.lower() == admin[0].lower() and contraseña == admin[1]:
            return "admin"
    for user in usuarios:
        if usuario.lower() == user[0].lower() and contraseña == user[1]:
            return "usuario"
    return None

def usuario_existente(nombre,usuarios,administradores,ignorar=None):
    for lista in (usuarios,administradores):
        for cuenta in lista:
            if cuenta is not ignorar and cuenta[0].lower()==nombre.lower():
                return True
    return False

def buscar_usuario_repetido(usuarios,administradores):
    vistos=[]
    for cuenta in usuarios+administradores:
        nombre=cuenta[0].lower()
        if nombre in vistos:
            return cuenta[0]
        vistos.append(nombre)
    return None