import inventario
from validaciones import leer_entero, leer_decimal, leer_texto

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

def menu_agregar_producto():
    codigo = leer_texto("Código del producto: ").upper()
    if inventario.buscar_indice_producto(codigo) != -1:
        print("Error: ya existe un producto con ese código.")
        return
    nombre = leer_texto("Nombre del producto: ")
    precio = leer_decimal("Precio: ", minimo=0.01)
    stock = leer_entero("Stock inicial: ", minimo=0)
    inventario.agregar_producto(codigo, nombre, precio, stock)
    print("Producto agregado correctamente.")

def menu_reabastecer():
    codigo = leer_texto("Código del producto: ").upper()
    pos = inventario.buscar_indice_producto(codigo)
    if pos == -1:
        print("Error: ese producto no existe.")
        return
    cantidad = leer_entero("Cantidad a sumar: ", minimo=1)
    if inventario.reabastecer_stock(pos, cantidad):
        print(f"Stock actualizado. Ahora hay {inventario.stocks[pos]} unidades.")
    else:
        print("No se pudo reabastecer.")