import inventario
carrito_nombres = []
carrito_cantidades = []
numero_factura = 1

def carrito_vacio():
    return len(carrito_nombres) == 0

def vaciar_carrito():
    carrito_nombres.clear()
    carrito_cantidades.clear()

def agregar_al_carrito(nombre, cantidad):
    pos = inventario.buscar_indice_producto(nombre)
    if pos == -1:
        print("error: ese producto no existe.")
        return False
    if cantidad <= 0:
        print("error: la cantidad debe ser mayor que 0.")
        return False
    
    # Cuánto de este producto ya está en el carrito
    nombre_real = inventario.nombres[pos]
    ya_en_carrito = 0
    if nombre_real in carrito_nombres:
        ya_en_carrito = carrito_cantidades[carrito_nombres.index(nombre_real)]
        
    disponible = inventario.stocks[pos] - ya_en_carrito
    if cantidad > disponible:
        print(f"error: stock insuficiente. Solo quedan {disponible} unidades disponibles.")
        return False
    
    if nombre_real in carrito_nombres:
        carrito_cantidades[carrito_nombres.index(nombre_real)] += cantidad
    else:
        carrito_nombres.append(nombre_real)
        carrito_cantidades.append(cantidad)
    return True

def mostrar_carrito():
    if carrito_vacio():
        print("\nTu carrito está vacío.")
        return 0
    total = 0
    print("\n" + "=" * 50)
    print(f"{'PRODUCTO':<22} | {'CANT':<5} | {'SUBTOTAL':>10}")
    print("=" * 50)
    for i in range(len(carrito_nombres)):
        pos = inventario.buscar_indice_producto(carrito_nombres[i])
        subtotal = inventario.precios[pos] * carrito_cantidades[i]
        total += subtotal
        print(f"{carrito_nombres[i]:<22} | {carrito_cantidades[i]:<5} | Bs{subtotal:>9.2f}")
    print("=" * 50)
    print(f"{'TOTAL':<31} Bs{total:>9.2f}")
    return total

def finalizar_compra(nombre_cliente):
    global numero_factura
    if carrito_vacio():
        print("No puedes pagar: tu carrito está vacío.")
        return None
    # 1) Revisar el stock antes de descontar 
    for i in range(len(carrito_nombres)):
        pos = inventario.buscar_indice_producto(carrito_nombres[i])
        if pos == -1 or carrito_cantidades[i] > inventario.stocks[pos]:
            print("Error: el stock cambió y ya no alcanza para algún producto.")
            return None
        
    # 2) Armar la factura y descontar stock
    total = 0
    lineas = []
    for i in range(len(carrito_nombres)):
        nombre = carrito_nombres[i]
        cantidad = carrito_cantidades[i]
        pos = inventario.buscar_indice_producto(nombre)
        precio = inventario.precios[pos]
        subtotal = precio * cantidad
        total += subtotal
        lineas.append(f"{nombre:<22} {cantidad:>4} {precio:>8.2f} {subtotal:>9.2f}")
        inventario.reducir_stock_por_nombre(nombre, cantidad)
    # 3) Factura
    ancho = 54
    print("\n" + "=" * ancho)
    print("FACTURA DE COMPRA".center(ancho))
    print("=" * ancho)
    print(f"Factura N°: {numero_factura:04d}")
    print(f"Cliente:    {nombre_cliente}")
    print("-" * ancho)
    print(f"{'PRODUCTO':<22} {'CANT':>4} {'P.UNIT':>8} {'SUBTOTAL':>9}")
    print("-" * ancho)
    for linea in lineas:
        print(linea)
    print("-" * ancho)
    print(f"{'TOTAL A PAGAR:':<{ancho - 10}}Bs{total:>8.2f}")
    print("=" * ancho)
    print("¡Gracias por su compra!".center(ancho))
    numero_factura += 1
    vaciar_carrito()
    return total

def quitar_del_carrito(codigo, cantidad):
    if codigo not in carrito_nombres:
        print("Error: ese producto no está en tu carrito.")
        return False
    i = carrito_nombres.index(codigo)
    if cantidad <= 0 or cantidad > carrito_cantidades[i]:
        print(f"error: puedes quitar entre 1 y {carrito_cantidades[i]} unidades.")
        return False
    if cantidad == carrito_cantidades[i]:
        # Se quita el producto de las DOS listas
        carrito_nombres.pop(i)
        carrito_cantidades.pop(i)
    else:
        carrito_cantidades[i] -= cantidad
    return True