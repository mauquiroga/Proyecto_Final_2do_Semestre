def ver_usuarios(usuarios):
    print("\n===== LISTA DE USUARIOS =====")
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    for i, user in enumerate(usuarios):
        print(f"\nID: {i}")
        print(f"Usuario: {user[0]}")
        print(f"Nombre: {user[2]}")
        print(f"Edad: {user[3]}")
def agregar_usuario(usuarios):
    print("\n===== AGREGAR USUARIO =====")
    usuario = input("Nuevo usuario: ")
    # Comprobar si ya existe
    for user in usuarios:
        if user[0].lower() == usuario.lower():
            print("Ese usuario ya existe.")
            return
    contraseña = input("Contraseña: ")
    nombre = input("Nombre completo: ")
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("La edad debe ser un número.")
        return
    usuarios.append([
        usuario,
        contraseña,
        nombre,
        edad
    ])
    print("Usuario agregado correctamente.")
def eliminar_usuario(usuarios):
    ver_usuarios(usuarios)
    if len(usuarios) == 0:
        return
    try:
        posicion = int(input("\nID del usuario a eliminar: "))
        if posicion < 0 or posicion >= len(usuarios):
            print("ID inválido.")
            return
        eliminado = usuarios.pop(posicion)
        print(f"Usuario '{eliminado[0]}' eliminado.")
    except ValueError:
        print("Debes introducir un número.")
def modificar_usuario(usuarios):
    ver_usuarios(usuarios)
    if len(usuarios) == 0:
        return
    try:
        posicion = int(input("\nID del usuario a modificar: "))
        if posicion < 0 or posicion >= len(usuarios):
            print("ID inválido.")
            return
        user = usuarios[posicion]
        print("\n¿Qué quieres modificar?")
        print("1. Usuario")
        print("2. Contraseña")
        print("3. Nombre")
        print("4. Edad")
        opcion = input("Opción: ")
        if opcion == "1":
            user[0] = input("Nuevo usuario: ")
        elif opcion == "2":
            user[1] = input("Nueva contraseña: ")
        elif opcion == "3":
            user[2] = input("Nuevo nombre: ")
        elif opcion == "4":
            try:
                user[3] = int(input("Nueva edad: "))
            except ValueError:
                print("La edad debe ser un número.")
                return
        else:
            print("Opción inválida.")
            return
        print("Usuario modificado correctamente.")
    except ValueError:
        print("Debes introducir un número.")