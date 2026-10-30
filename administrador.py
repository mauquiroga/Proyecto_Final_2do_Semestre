import inventario
from validaciones import leer_entero, leer_decimal, leer_texto, confirmar

def ver_usuarios(usuarios):
    print("\n LISTA DE USUARIOS")
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    for i, user in enumerate(usuarios):
        print(f"\nID: {i+1}")
        print(f"Usuario: {user[0]}")
        print(f"Nombre: {user[2]}")
        print(f"Edad: {user[3]}")

def agregar_usuario(usuarios):
    print("\n AGREGAR USUARIO")
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
    name_user=input("ingrese usuario a eliminar: ").strip().lower()
    for i in range(len(usuarios)):
        if usuarios[i][0].lower() == name_user:
            confirmar=input("confirmar eleminar usuario (s/n): ")
            if confirmar == "s":
                usuarios.pop(i)
                print("usuario eliminado correctamente")
            else:
                print("operacion cancelada")
                return
    print("error: usuario no existente")

def modificar_usuario(usuarios):
    ver_usuarios(usuarios)
    if len(usuarios) == 0:
        return
    usuario=input("\n ingrese usuario a modificar: ").strip().lower()
    user=None
    for u in usuarios:
        if u[0].lower() == usuario:
            user=u
            break
    if user is None:
        print("error: el usuario no existe")
        return 
    while True:   
        print("\n¿Qué quieres modificar?")
        print("1. Usuario")
        print("2. Contraseña")
        print("3. Nombre")
        print("4. Edad")
        print("5. Volver")
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
        elif opcion == "5":
            break    
        else:
            print("Opción inválida.")
            return
        print("Usuario modificado correctamente.")

def menu_agregar_producto():
    while True:
        codigo = leer_texto("Código del producto: ").upper()
        if inventario.buscar_indice_producto(codigo) != -1:
            print("Error: ya existe un producto con ese código.")
            return
        else:
            nombre = leer_texto("Nombre del producto: ")
            precio = leer_decimal("Precio: ", minimo=0.01)
            stock = leer_entero("Stock inicial: ", minimo=0)
            inventario.agregar_producto(codigo, nombre, precio, stock)
            print("Producto agregado correctamente.")
        if not confirmar("Quieres agregar otro producto?"):
            break

def menu_reabastecer():
    while True:
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
        if not confirmar("reabastecer otro producto?"):
            break

def menu_eliminar_producto():
    while True:
        inventario.mostrar_catalogo()
        codigo = leer_texto("Código del producto a eliminar: ").upper()
        pos = inventario.buscar_indice_producto(codigo)
        if pos == -1:
            print("error: ese producto no existe.")
            continue
        nombre = inventario.nombres[pos]
        if confirmar(f"¿Seguro que quieres eliminar '{nombre}'?"):
            inventario.eliminar_producto(codigo)
            print("Producto eliminado.")
        else:
            print("Operación cancelada.")
        if not confirmar("Quieres eleminar otro producto?"):
            break

def menu_cuentas(usuarios):
    while True:
        print("\n ADMINISTRAR CUENTAS")
        print("1. Ver usuarios")
        print("2. Agregar usuario")
        print("3. Eliminar usuario")
        print("4. Modificar usuario")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                ver_usuarios(usuarios)
            case "2":
                agregar_usuario(usuarios)
            case "3":
                eliminar_usuario(usuarios)
            case "4":
                modificar_usuario(usuarios)
            case "5":
                break
            case _:
                print("Opción inválida.")

def menu_tienda_admin():
    while True:
        print("\n ADMINISTRAR TIENDA")
        print("1. Ver catálogo")
        print("2. Agregar producto")
        print("3. Reabastecer stock")
        print("4. Eliminar producto")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                inventario.mostrar_catalogo()
            case "2":
                menu_agregar_producto()
            case "3":
                menu_reabastecer()
            case "4":
                menu_eliminar_producto()
            case "5":
                break
            case _:
                print("Opción inválida.")