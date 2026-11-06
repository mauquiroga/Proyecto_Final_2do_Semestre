# Listas para almacenar la información de los productos
codigos = ["A1", "A2", "B1", "B2", "C1"]
nombres = ["Chocolate", "Gomitas acidas", "Papas Fritas", "Cereal", "Refresco en Lata"]
precios = [2.50, 1.75, 2.00, 1.50, 2.25]
stocks = [5, 8, 4, 10, 6]

def mostrar_catalogo():
    if len(nombres) == 0:
        print("\nEl catálogo está vacío.")
        return
    print("\n" + "=" * 45)
    print(f"{'PRODUCTO':<22} | {'PRECIO':<8} | {'STOCK':<6}")
    print("=" * 45)
    for i in range(len(nombres)):
        print(f"{nombres[i]:<22} | Bs{precios[i]:<6.2f} | {stocks[i]:<6}")
    print("=" * 45)

def buscar_indice_producto(nombre):
    nombre_limpio = nombre.strip().lower()
    for i in range(len(nombres)):
        if nombres[i].strip().lower() == nombre_limpio:
            return i
    return -1

def reabastecer_stock(pos, cantidad):
    if 0 <= pos < len(stocks):
        stocks[pos] += cantidad
        return True
    return False

def agregar_producto(nombre, precio, stock):
    nombres.append(nombre)
    precios.append(float(precio))
    stocks.append(int(stock))

def reducir_stock_por_nombre(nombre, cantidad):
    pos = buscar_indice_producto(nombre)
    if pos != -1 and stocks[pos] >= cantidad:
        stocks[pos] -= cantidad
        return True
    return False

def eliminar_producto(nombre):
    pos = buscar_indice_producto(nombre)
    if pos != -1:
        nombres.pop(pos)
        precios.pop(pos)
        stocks.pop(pos)
        return True
    return False