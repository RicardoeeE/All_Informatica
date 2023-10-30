a =0
b =a
while True:
    print("\nMenú:")
    print("1. Calcular primorial")
    print("2. Comprobar omirp")
    print("3. Comprobar abundante ")
    print("4. Salir")

    opcion = input("Escoja una de las opciones anteriores: ")

    if opcion == "1":
        # Código para la opción 1
        print("\nSeleccionaste la opción 1")
        print(f"El primorial de {a} vale {b} ")

    elif opcion == "2":
        # Código para la opción 2
        print("Seleccionaste la opción 2")
    elif opcion == "3":
        # Código para la opción 3
        print("Seleccionaste la opción 3")
    elif opcion == "4":
        print("Saliendo del menú.")
        break
    else:
        print("Opción incorrecta. Vuelva a intentarlo: ")
