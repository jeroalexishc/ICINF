notas = [] 

while True: 
    nota = float(input("Ingrese una nota (0 para finalizar): "))
    if nota == 0:
        break
    notas.append(nota)

if len(notas) > 0: 
    cantidad_notas = len(notas) 
    promedio_notas = sum(notas) / cantidad_notas 
    nota_minima = min(notas) 
    nota_maxima = max(notas) 

    print("1) Cantidad de notas:", cantidad_notas) 
    print("2) Promedio de notas:", promedio_notas)
    print("3) La nota mínima:", nota_minima)
    print("4) La nota máxima:", nota_maxima)
else:
    print("No se ingresaron notas.")