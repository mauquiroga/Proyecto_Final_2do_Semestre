# Listas para almacenar la información de los productos
codigos = ["A1", "A2", "B1", "B2", "C1"]
nombres = ["Chocolate", "Gomitas acidas", "Papas Fritas", "Cereal", "Refresco en Lata"]
precios = [2.50, 1.75, 2.00, 1.50, 2.25]
stocks = [5, 8, 4, 10, 6]

def mostrar_catalogo():
    print("\n" + "="*55)
    print(f"{'INDICE':<8} | {'CODIGO':<8} | {'PRODUCTO':<22} | {'PRECIO':<7} | {'STOCK':<5}")
    print("="*55)
    for i in range(len(codigos)):
        print(f"{i:<8} | {codigos[i]:<8} | {nombres[i]:<22} | Bs{precios[i]:<5.2f} | {stocks[i]:<5}")
    print("="*55)

def buscar_indice_producto(codigo_buscado):
    for i in range(len(codigos)):
        if codigos[i] == codigo_buscado:
            return i
    return -1

def reabastecer_stock(posicion, cantidad):
    if posicion != -1 and cantidad > 0:
        stocks[posicion] = stocks[posicion] + cantidad
        return True
    return False

def agregar_producto(nuevo_cod, nuevo_nombre, nuevo_precio, nuevo_stock):
    codigos.append(nuevo_cod)
    nombres.append(nuevo_nombre)
    precios.append(nuevo_precio)
    stocks.append(nuevo_stock)

def reducir_stock_por_codigo(codigo_buscado, cantidad=1):
    pos = buscar_indice_producto(codigo_buscado)
    if pos != -1 and cantidad > 0 and stocks[pos] >= cantidad:
        stocks[pos] -= cantidad
        return True
    return False

def eliminar_producto(codigo_buscado):
    pos = buscar_indice_producto(codigo_buscado)
    if pos == -1:
        return False
    codigos.pop(pos)
    nombres.pop(pos)
    precios.pop(pos)
    stocks.pop(pos)
    return True