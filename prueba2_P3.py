paises_capitales = {}

for i in range(5): 
    pais = input("Ingrese el nombre del país " + str(i+1) + ": ")
    capital = input("Ingrese la capital de " + pais + ": ")
    paises_capitales[pais] = capital

nombre_turista = input("Ingrese el nombre del turista: ")
pais_procedencia = input("Ingrese el país de procedencia del turista: ")

if pais_procedencia in paises_capitales: 
    capital = paises_capitales[pais_procedencia]
    texto = "El turista con el nombre " + nombre_turista + " viene del país " + pais_procedencia + " y su capital es " + capital
    print(texto)
else:
    print("El país de procedencia no está en la lista de países ingresados.")