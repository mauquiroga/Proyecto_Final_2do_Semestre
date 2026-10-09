import funciones

def user0(usuario,contraseña):
    a="user"
    b="12345"
    if usuario==a and contraseña==b:
        return True
    else:
        return False

def menu_usuario():
    while True:
        try:

            print("----Menu Usuario----")
            print("-------------------------")
            print("1.Ver informacion.")
            print("2.Consultar datos.")
            print("3.Realizar una operacion.")
            print("4.Cerrar sesion.")
            print("--------------------------")
            opcion=int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    print("Ver informacion")
                case 2:
                    print("Consultar datos...")
                case 3:
                    print("Realizar una operacion...")
                case 4:
                    print("Saliendo....")
                    funciones.login()
                case _:
                    print("Opcion no valida")
        except ValueError:
            print("Valor no valido")