print("Ejercicio 2: Menu de la cafetria cute")
print("Nombre: Axel Adriel Ramirez Quintanilla")
print("Matricula: AL07310252")
print()

# while True: el menú se repite siempre; la única salida es el break
while True:
    # Mostramos el menú
    print()
    print(" ===== CAFETERIA CUTE ===== ")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")

    # Pedimos la opción
    opcion = input("Elige una opción: ")

    # Revisamos qué opción eligió
    if opcion == "1":
        print("Frappé de cajeta.....$65")
        print("Matcha latte........$78")
        print("Smoothie de fresa...$55")
    elif opcion == "2":
        print("Galleta red velvet..$35")
        print("Cupcake de Oreo.....$40")
        print("Dona glaseada.......$30")
    elif opcion == "3":
        print("Lunes a viernes: 7:00 a 20:00")
        print("Sábados: 9:00 a 14:00")
    elif opcion == "4":
        print("¡Gracias por visitarnos!")
        # El cliente eligió Salir: break nos saca del while
        break

    else:
        print("X Opción no válida, elige del 1 al 4")