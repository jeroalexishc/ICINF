def convierte_negativo(lista):
    for i in range(len(lista)):
        lista[i] = -lista[i]
    return lista

numeros = []

print("Ingrese 10 números enteros positivos:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Número {i+1}: "))
            if num > 0:
                numeros.append(num)
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

print("\nLista original:", numeros)

numeros_negativos = convierte_negativo(numeros)

print("Lista con números convertidos a negativo:", numeros_negativos)