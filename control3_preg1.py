def solo_numeros(var):
    if var == "":
        return False
    numeros = "0123456789"
    for i in range(len(var)):
        if var[i] not in numeros:
            return False
    return True

while True:
    entrada = input("Ingrese una cadena (o 'salir' para terminar): ")
    
    if entrada == "salir":
        print("Programa terminado.")
        break
    
    resultado = solo_numeros(entrada)
    
    if resultado == True:
        print("'" + entrada + "' contiene solo números.")
    else:
        print("'" + entrada + "' NO contiene solo números.")