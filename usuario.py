import inventario
import carrito
from validaciones import leer_entero, leer_texto, confirmar

def ver_perfil(usuario):
    print("\n===== MI PERFIL =====")
    print(f"Usuario: {usuario[0]}")
    print(f"Nombre: {usuario[2]}")
    print(f"Edad: {usuario[3]}")

def cambiar_contraseña(usuario):
    print("\n===== CAMBIAR CONTRASEÑA =====")
    nueva = input("Nueva contraseña: ")
    usuario[1] = nueva
    print("Contraseña actualizada correctamente.")

def cambiar_nombre(usuario):
    print("\n===== CAMBIAR NOMBRE =====")
    nuevo = input("Nuevo nombre: ")
    usuario[2] = nuevo
    print("Nombre actualizado correctamente.")

def menu_agregar_carrito():
    while True:
        inventario.mostrar_catalogo()
        codigo = leer_texto("Código del producto: ").upper()
        cantidad = leer_entero("Cantidad: ", minimo=1)
        if carrito.agregar_al_carrito(codigo, cantidad):
            print("Producto agregado al carrito.")
        if not confirmar("Quieres agregar otro producto: "):
            break

def menu_pagar(usuario_actual):
    carrito.mostrar_carrito()
    if carrito.carrito_vacio():
        return
    confirmar = input("¿Confirmar compra? (s/n): ").strip().lower()
    if confirmar == "s":
        carrito.finalizar_compra(usuario_actual[2])
    else:
        print("Compra cancelada.")

def menu_quitar_carrito():
    while True:
        if carrito.carrito_vacio():
            print("Tu carrito está vacío.")
            break
        carrito.mostrar_carrito()
        codigo = leer_texto("Código del producto a quitar: ").upper()
        if codigo not in carrito.carrito_codigos:
            print("Ese producto no está en tu carrito.")
            continue
        i = carrito.carrito_codigos.index(codigo)
        maximo = carrito.carrito_cantidades[i]
        cantidad = leer_entero(f"¿Cuántas unidades quitar? (1-{maximo}): ",
            minimo=1,
            maximo=maximo)
        if carrito.quitar_del_carrito(codigo, cantidad):
            print("Carrito actualizado.")
        if carrito.carrito_vacio():
            print("tu carrito quedo vacio")
            break
        if not confirmar("quieres quitar otro producto?"):
            break

def menu_cuenta(usuario_actual):
    while True:
        print("\n===== MI CUENTA =====")
        print("1. Ver mi información")
        print("2. Cambiar nombre")
        print("3. Cambiar contraseña")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                ver_perfil(usuario_actual)
            case "2":
                cambiar_nombre(usuario_actual)
            case "3":
                cambiar_contraseña(usuario_actual)
            case "4":
                break
            case _:
                print("Opción inválida.")

def menu_tienda_usuario(usuario_actual):
    while True:
        print("\n===== TIENDA =====")
        print("1. Ver catálogo")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Quitar del carrito")
        print("5. Pagar")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                inventario.mostrar_catalogo()
            case "2":
                menu_agregar_carrito()
            case "3":
                carrito.mostrar_carrito()
            case "4":
                menu_quitar_carrito()
            case "5":
                menu_pagar(usuario_actual)
            case "6":
                break
            case _:
                print("Opción inválida.")