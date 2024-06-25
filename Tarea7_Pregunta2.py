palabras = []

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras.append(palabra)

print("\nResultados:")
for palabra in palabras:
    cuenta_A = 0
    cuenta_a = 0
    for letra in palabra:
        if letra == 'A':
            cuenta_A += 1
        elif letra == 'a':
            cuenta_a += 1
    
    total_a = cuenta_A + cuenta_a
    print("'" + palabra + "' tiene " + str(total_a) + " letra(s) 'A' o 'a' ")
    print("  'A' mayuscula: " + str(cuenta_A))
    print("  'a' minuscula: " + str(cuenta_a))



