def separar(lista):
    pares = sorted([num for num in lista if num % 2 == 0])
    impares = sorted([num for num in lista if num % 2 != 0])
    return pares, impares

numeros = [6, 5, 2, 1, 7]
pares, impares = separar(numeros)
print(pares)
print(impares)