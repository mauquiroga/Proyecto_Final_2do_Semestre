import inventario
from datos import administradores
from login import usuario_existente
from validaciones import leer_entero, leer_decimal, leer_texto, confirmar

def ver_usuarios(usuarios):
    print("\n===== LISTA DE USUARIOS =====")
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    for i, user in enumerate(usuarios):
        print(f"\nID: {i+1}")
        print(f"Usuario: {user[0]}")
        print(f"Nombre: {user[2]}")
        print(f"Edad: {user[3]}")

def agregar_usuario(usuarios):
    while True:
        print("\n===== AGREGAR USUARIO =====")
        usuario = input("Nuevo usuario: ")
        if usuario_existente(usuario,usuarios,administradores):
            print("ese usuario ya esta en uso")
            continue
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
        if not confirmar("quieres agregar otro usuario?"):
            break

def eliminar_usuario(usuarios):
    while True:
        ver_usuarios(usuarios)
        if len(usuarios) == 0:
            return
        name_user=input("ingrese usuario a eliminar: ").strip().lower()
        encontrado=False
        for i in range(len(usuarios)):
            if usuarios[i][0].lower() == name_user:
                encontrado=True
                if confirmar("confirmar para eleminar el usuario"):
                    usuarios.pop(i)
                    print("usuario eliminado correctamente")
                else:
                    print("operacion cancelada")
                    break
        if not encontrado:
            print("ese usuario no existe")
        if not confirmar("quieres eliminar otro usuario?"):
            break

def modificar_usuario(usuarios):
    while True:
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
                nuevo = input("Nuevo usuario: ")
                if usuario_existente(nuevo,usuarios,administradores,ignorar=user):
                    print("error: ese usuario ya existe")
                else:
                    user[0]=nuevo
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
            if not confirmar("quieres modificar otro dato?"):
                break
        if not confirmar("quieres modificar otro usuario?"):
            break

def menu_agregar_producto():
    while True:
        nombre = leer_texto("Nombre del producto: ")
        # Cambio: Se verifica si el producto ya existe por su nombre
        if inventario.buscar_indice_producto(nombre) != -1:
            print("Error: ya existe un producto con ese nombre.")
        else:
            precio = leer_decimal("Precio: ", minimo=0.01)
            stock = leer_entero("Stock inicial: ", minimo=0)
            inventario.agregar_producto(nombre, precio, stock)
            print("Producto agregado correctamente.")
        if not confirmar("¿Quieres agregar otro producto?"):
            break

def menu_reabastecer():
    while True:
        inventario.mostrar_catalogo()
        nombre = leer_texto("Nombre del producto a reabastecer: ")
        pos = inventario.buscar_indice_producto(nombre)
        if pos == -1:
            print("Error: ese producto no existe.")
        else:
            cantidad = leer_entero("Cantidad a sumar: ", minimo=1)
            if inventario.reabastecer_stock(pos, cantidad):
                print(f"Stock actualizado. Ahora hay {inventario.stocks[pos]} unidades.")
            else:
                print("No se pudo reabastecer.")
        if not confirmar("¿Reabastecer otro producto?"):
            break

def menu_eliminar_producto():
    while True:
        inventario.mostrar_catalogo()
        nombre = leer_texto("Nombre del producto a eliminar: ")
        pos = inventario.buscar_indice_producto(nombre)
        if pos == -1:
            print("Error: ese producto no existe.")
            continue
        nombre_real = inventario.nombres[pos]
        if confirmar(f"¿Seguro que quieres eliminar '{nombre_real}'?"):
            # Cambio: Se elimina pasándole el nombre al módulo inventario
            if inventario.eliminar_producto(nombre_real):
                print("Producto eliminado.")
            else:
                print("Error al eliminar el producto.")
        else:
            print("Operación cancelada.")
        if not confirmar("¿Quieres eliminar otro producto?"):
            break

def menu_cuentas(usuarios,admin_actual):
    while True:
        print("\n===== ADMINISTRAR CUENTAS =====")
        print("1. Ver usuarios")
        print("2. Agregar usuario")
        print("3. Eliminar usuario")
        print("4. Modificar usuario")
        print("5. ver administradores")
        print("6. agregar admins")
        print("7. eliminar admins")
        print("8. Volver")
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
                ver_administradoes()
            case "6":
                agregar_admin(usuarios)
            case "7":
                eliminar_admin(admin_actual)
            case "8":
                break
            case _:
                print("Opción inválida.")

def menu_tienda_admin():
    while True:
        print("\n===== ADMINISTRAR TIENDA =====")
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

def ver_administradoes():
    print("\n===== ADMINISTRADORES =====")
    for i in range(len(administradores)):
        print(f"{i+1}. {administradores[i][0]}-{administradores[i][2]}")

def agregar_admin(usuarios):
    while True:
        print("\n===== AGREGAR ADMINISTRADOR =====")
        nuevo=input("ingrese nuevo admin(usuario): ")
        if usuario_existente(nuevo,usuarios,administradores):
            print("ese usuario ya esta en uso")
            continue
        clave=input("ingrese contraseña: ")
        nombre=input("ingrese nombre completo: ")
        administradores.append([nuevo, clave, nombre])
        print("admin agregado exitosamente")
        if not confirmar("quieres agregar otro admin?"):
            break
def eliminar_admin(admin_actual):
    while True:
        if len(administradores)<=1:
            print("no puedes eleminar al ultimo admin que queda")
            break
        ver_administradoes()
        user=input("ingrese el admin a eleminar(usuario): ").lower()
        encontrado=None
        for a in administradores:
            if a[0].lower()==user:
                encontrado=a
                break
        if encontrado is None:
            print("error: ese admin no existe")
        elif user == admin_actual.lower():
            print("error: no puedes eleminar tu cuenta activa")
        elif confirmar(f"seguro de querer eliminar a {encontrado[0]}?"):
            administradores.remove(encontrado)
            print("admin eliminado")
        else:
            print("operacion cancelada")
        if not confirmar("quieres eleminar otro admin?"):
            break                
