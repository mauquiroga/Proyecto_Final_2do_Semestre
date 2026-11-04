def iniciar_sesion(usuario, contraseña, usuarios, administradores):
    for admin in administradores:
        if usuario.lower() == admin[0].lower() and contraseña == admin[1]:
            return "admin"
    for user in usuarios:
        if usuario.lower() == user[0].lower() and contraseña == user[1]:
            return "usuario"
    return None