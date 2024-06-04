lista = []

while True:
    print("Elija una opción: ")
    print("1. Ingresar un elemento a la lista ")
    print("2. Modificar un elemento de la lista según índice ")
    print("3. Eliminar un elemento de la lista según índice ")
    print("4. Eliminar el último elemento de la lista ")
    print("5. Buscar un elemento de la lista ")
    print("6. Mostrar todos los elementos de la lista ")
    print("7. Salir ")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        lista.append(elemento)
        print("")
        print("_____________________________")
        print("")
        print("Elemento agregado a la lista.")
        print("_____________________________")
        print("")

    elif opcion == "2":
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if indice >= 0 and indice < len(lista):
            nuevo_elemento = input("Ingrese el nuevo valor: ")
            lista[indice] = nuevo_elemento
            print("")
            print("________________________________")
            print("")
            print("Elemento modificado en la lista.")
            print("________________________________")
            print("")
        else:
            print("Índice fuera de rango.")

    elif opcion == "3":
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if indice >= 0 and indice < len(lista):
            elemento_eliminado = lista.pop(indice)
            print("")
            print("_____________________________________________________")
            print("")
            print(f"Elemento '{elemento_eliminado}' eliminado de la lista.")
            print("_____________________________________________________")
            print("")
        else:
            print("")
            print("_____________________")
            print("")
            print("Índice fuera de rango.")
            print("_____________________")
            print("")

    elif opcion == "4":
        if lista:
            elemento_eliminado = lista.pop()
            print("")
            print("_____________________")
            print("")
            print(f"Elemento '{elemento_eliminado}' eliminado de la lista.")
            print("_____________________")
            print("")
        else:
            print("")
            print("_____________________")
            print("")
            print("La lista está vacía.")
            print("_____________________")
            print("")

    elif opcion == "5":
        elemento = input("Ingrese el elemento a buscar: ")
        if elemento in lista:
            indice = lista.index(elemento)
            print("")
            print("____________________________________________")
            print("")
            print(f"El elemento '{elemento}' está en el índice numero {indice}.")
            print("____________________________________________")
            print("")
        else:
            print("")
            print("____________________________________________")
            print("")
            print(f"El elemento '{elemento}' no se encuentra en la lista.")
            print("____________________________________________")
            print("")

    elif opcion == "6":
        if lista:
            print("")
            print("_____________________")
            print("")
            print("Lista actual:")
            print("")
            print(lista)
            print("")
            print("Elementos en la lista:")
            for i, elemento in enumerate(lista):
                print(f"{i}. {elemento}")
            print("_____________________")
            print("")
        else:
            print("")
            print("_____________________")
            print("")
            print("La lista está vacía.")
            print("_____________________")
            print("")

    elif opcion == "7":
        print("")
        print("_____________________")
        print("")
        print("Programa Finalizado")
        print("_____________________")
        print("")
        break

    else:
        print("")
        print("___________________________________")
        print("")
        print("Opción inválida. Intente nuevamente.")
        print("___________________________________")
        print("")