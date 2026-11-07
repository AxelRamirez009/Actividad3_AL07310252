print("Ejercicio 1: Inicia sesion en Roblox")
print("Nombre: Axel Adriel Ramirez Quintanilla")
print("Matricula: AL07310252")
print()

# Guardamos el usuario y la contraseña correctos
usuario_correcto = "AxelPerdoro"
contrasena_correcta = "axel123"

# Al inicio todavía NO ha iniciado sesión
sesion_iniciada = False

# Mientras NO haya iniciado sesión, se repite
while sesion_iniciada == False:
    # Pedimos el usuario y la contraseña
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    # ¿EL usuario es IGUAL al correcto?
    if usuario == usuario_correcto:
        # Si existe. Ahora: ¿la contraseña es IGUAL a la correcta?
        if contrasena == contrasena_correcta:
            print(" ¡Bienvenido,", usuario, "!")
            # Ya entró: esto hace que el while se detenga
            sesion_iniciada = True
        else:
            print("X La contraseña es incorrecta")
    else:
        print("X Ese usuario no existe")
        
# Esto se ejecuta cuando ya salió del while
print("Cargando tus juegos ... ")