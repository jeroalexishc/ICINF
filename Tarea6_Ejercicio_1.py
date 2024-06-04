lista = []

while True:
    palabra = input("Ingresar palabra (Enter para finalizar): ")
    if palabra == "":
        break
    lista.append(palabra)

for palabra in lista:
    vocales = 0
    consonantes = 0
    
    for letra in palabra:

        if letra.lower() in "aeiou":
            vocales += 1
        else:
            consonantes += 1
            
    print(f"La palabra '{palabra}' tiene {vocales} vocal(es) y {consonantes} consonante(s).")