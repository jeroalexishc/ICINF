def sumatoria(numero):
    if numero <= 1:
        return numero
    else:
        return numero + sumatoria(numero - 1)

numero = 100
resultado = sumatoria(numero)
print(f"La sumatoria de {numero} es {resultado}")