def leer_entero(mensaje, minimo=None, maximo=None):
    #Pide un entero y repite hasta que sea válido. Nunca lanza ValueError
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("error: escribe un número entero (sin letras ni decimales).")
            continue
        if minimo is not None and valor < minimo:
            print(f"error: el valor debe ser como mínimo {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"error: el valor debe ser como máximo {maximo}.")
            continue
        return valor

def leer_decimal(mensaje, minimo=None):
    #Pide un número decimal (acepta coma o punto) y repite hasta que sea válido
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("error: escribe un número válido, por ejemplo 2.50")
            continue
        if minimo is not None and valor < minimo:
            print(f"error: el valor debe ser como mínimo {minimo}.")
            continue
        return valor

def leer_texto(mensaje):
    #Pide un texto que no esté vacío.
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("error: este campo no puede estar vacío.")

def confirmar(mensaje):
    while True:
        s_n=input(mensaje + "(s/n): ").strip().lower()
        if s_n == "s":
            return True
        elif s_n == "n":
            return False
        print("responder solo 's' o 'n'")