p=int(input("ingrese la cantidad de preguntas: "))
q=int(input("ingrese la cantidad de preguntas correctas: "))

nivel=(q*100)/p

if nivel >=95:
    print("Nivel Maximo: ", nivel,"%")
else:
    if nivel >= 70 and nivel < 95:
        print("Nivel Medio: ", nivel,"%")
    else:
        if nivel >= 40 and nivel < 70:
            print("Nivel Regular: ", nivel,"%")
        else:
            if nivel < 40:
                print("Fuera de nivel: ", nivel,"%")