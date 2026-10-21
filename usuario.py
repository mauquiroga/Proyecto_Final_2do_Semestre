import inventario
import carrito
from validaciones import leer_entero, leer_texto

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
    inventario.mostrar_catalogo()
    codigo = leer_texto("Código del producto: ").upper()
    cantidad = leer_entero("Cantidad: ", minimo=1)
    if carrito.agregar_al_carrito(codigo, cantidad):
        print("Producto agregado al carrito.")

def menu_pagar(usuario_actual):
    carrito.mostrar_carrito()
    if carrito.carrito_vacio():
        return
    confirmar = input("¿Confirmar compra? (s/n): ").strip().lower()
    if confirmar == "s":
        carrito.finalizar_compra(usuario_actual[2])
    else:
        print("Compra cancelada.")