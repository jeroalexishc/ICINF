# Ingresar un numero e identificar la cantidad de digitos, desde el 1 hasta el 9999:

num=int(input("ingrese un numero "))

if num >= 0 and num < 10000:

    if num < 10:
        print("el numero tiene 1 digito ")
    else:
        if num < 100:
            print("el numero tiene 2 digitos ")
        else:
            if num < 1000:
                print("el numero tiene 3 digitos ")
            else:
                if num < 10000:
                    print("el numero tiene 4 digitos ")
else:
    print("numero fuera de rango ")
