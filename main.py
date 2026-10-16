from datos import usuarios, administradores
from login import iniciar_sesion
from administrador import (
    ver_usuarios,
    agregar_usuario,
    eliminar_usuario,
    modificar_usuario
)
from usuario import (
    ver_perfil,
    cambiar_contraseña,
    cambiar_nombre
)
while True:
    print("\n==============================")
    print("       SISTEMA DE LOGIN")
    print("==============================")
    usuario_login = input("Usuario: ")
    contraseña = input("Contraseña: ")
    tipo = iniciar_sesion(
        usuario_login,
        contraseña,
        usuarios,
        administradores
    )
    # ADMINISTRADOR
    if tipo == "admin":
        print("\nBienvenido administrador.")
        while True:
            print("\n===== MENU ADMINISTRADOR =====")
            print("1. Ver usuarios")
            print("2. Agregar usuario")
            print("3. Eliminar usuario")
            print("4. Modificar usuario")
            print("5. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ver_usuarios(usuarios)
            elif opcion == "2":
                agregar_usuario(usuarios)
            elif opcion == "3":
                eliminar_usuario(usuarios)
            elif opcion == "4":
                modificar_usuario(usuarios)
            elif opcion == "5":
                print("Sesión cerrada.")
                break
            else:
                print("Opción inválida.")
    # USUARIO
    elif tipo == "usuario":
        # Buscar al usuario que inició sesión
        usuario_actual = None
        for user in usuarios:
            if user[0].lower() == usuario_login.lower():
                usuario_actual = user
                break
        print("\nBienvenido", usuario_actual[2])
        while True:
            print("\n===== MENU USUARIO =====")
            print("1. Ver mi información")
            print("2. Cambiar nombre")
            print("3. Cambiar contraseña")
            print("4. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ver_perfil(usuario_actual)
            elif opcion == "2":
                cambiar_nombre(usuario_actual)
            elif opcion == "3":
                cambiar_contraseña(usuario_actual)
            elif opcion == "4":
                print("Sesión cerrada.")
                break
            else:
                print("Opción inválida.")
    else:
        print("\nUsuario o contraseña incorrectos.")