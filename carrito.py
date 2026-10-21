import inventario
carrito_codigos = []
carrito_cantidades = []
numero_factura = 1

def carrito_vacio():
    return len(carrito_codigos) == 0

def vaciar_carrito():
    carrito_codigos.clear()
    carrito_cantidades.clear()

def agregar_al_carrito(codigo, cantidad):
    pos = inventario.buscar_indice_producto(codigo)
    if pos == -1:
        print("error: ese producto no existe.")
        return False
    if cantidad <= 0:
        print("error: la cantidad debe ser mayor que 0.")
        return False
    # Cuánto de este producto ya está en el carrito
    ya_en_carrito = 0
    if codigo in carrito_codigos:
        ya_en_carrito = carrito_cantidades[carrito_codigos.index(codigo)]
    disponible = inventario.stocks[pos] - ya_en_carrito
    if cantidad > disponible:
        print(f"error: stock insuficiente. Solo quedan {disponible} unidades disponibles.")
        return False
    if codigo in carrito_codigos:
        carrito_cantidades[carrito_codigos.index(codigo)] += cantidad
    else:
        carrito_codigos.append(codigo)
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
    for i in range(len(carrito_codigos)):
        pos = inventario.buscar_indice_producto(carrito_codigos[i])
        subtotal = inventario.precios[pos] * carrito_cantidades[i]
        total += subtotal
        print(f"{inventario.nombres[pos]:<22} | {carrito_cantidades[i]:<5} | Bs{subtotal:>9.2f}")
    print("=" * 50)
    print(f"{'TOTAL':<31} Bs{total:>9.2f}")
    return total

def finalizar_compra(nombre_cliente):
    #Valida stock, descuenta, imprime la factura y vacía el carrito.
    global numero_factura
    if carrito_vacio():
        print("No puedes pagar: tu carrito está vacío.")
        return None
    # 1) Revisar el stock antes de descontar 
    for i in range(len(carrito_codigos)):
        pos = inventario.buscar_indice_producto(carrito_codigos[i])
        if pos == -1 or carrito_cantidades[i] > inventario.stocks[pos]:
            print("Error: el stock cambió y ya no alcanza para algún producto.")
            print("Revisa tu carrito y vuelve a intentarlo.")
            return None
    # 2) Armar la factura y descontar stock
    total = 0
    lineas = []
    for i in range(len(carrito_codigos)):
        codigo = carrito_codigos[i]
        cantidad = carrito_cantidades[i]
        pos = inventario.buscar_indice_producto(codigo)
        nombre = inventario.nombres[pos]
        precio = inventario.precios[pos]
        subtotal = precio * cantidad
        total += subtotal
        lineas.append(f"{codigo:<6} {nombre:<20} {cantidad:>4} {precio:>8.2f} {subtotal:>9.2f}")
        inventario.reducir_stock_por_codigo(codigo, cantidad)
    # 3) Factura
    ancho = 52
    print("\n" + "=" * ancho)
    print("FACTURA DE COMPRA".center(ancho))
    print("=" * ancho)
    print(f"Factura N°: {numero_factura:04d}")
    print(f"Cliente:    {nombre_cliente}")
    print("-" * ancho)
    print(f"{'COD':<6} {'PRODUCTO':<20} {'CANT':>4} {'P.UNIT':>8} {'SUBTOTAL':>9}")
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