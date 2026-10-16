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