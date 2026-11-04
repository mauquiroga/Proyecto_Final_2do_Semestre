import carrito
from datos import usuarios, administradores
from login import iniciar_sesion
from administrador import menu_cuentas, menu_tienda_admin
from usuario import menu_cuenta, menu_tienda_usuario
while True:
    print("\n" + "=" * 32)
    print("             LOGIN")
    print("=" * 32)
    usuario_login = input("Usuario: ")
    contraseña = input("Contraseña: ")
    tipo = iniciar_sesion(usuario_login,contraseña,usuarios,administradores)
    # ADMINISTRADOR
    if tipo == "admin":
        print("\nBienvenido administrador.")
        while True:
            print("\n===== MENU ADMINISTRADOR =====")
            print("1. Administrar cuentas")
            print("2. Administrar tienda")
            print("3. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    menu_cuentas(usuarios)
                case "2":
                    menu_tienda_admin()
                case "3":
                    print("Sesión cerrada.")
                    break
                case _:
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
            print("1. Mi cuenta")
            print("2. Tienda")
            print("3. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    menu_cuenta(usuario_actual)
                case "2":
                    menu_tienda_usuario(usuario_actual)
                case "3":
                    carrito.vaciar_carrito()
                    print("Sesión cerrada.")
                    break
                case _:
                    print("Opción inválida.")
    else:
        print("\nUsuario o contraseña incorrectos.")