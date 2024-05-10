# Identificar la cantidad de digitos de un numero ingresado, en un rango desde el numero 1 hasta el 9999:

num=int(input("ingrese un numero "))

if num >= 0 and num < 10:
    print("el numero tiene solo 1 digito ")
elif num >= 10 and num < 100:
    print("el numero tiene 2 digitos ")
elif num >= 100 and num < 1000:
    print("el numero tiene 3 digitos ")
elif num >= 1000 and num < 10000:
    print("el numero tiene 4 digitos ")
else:
    num > 9999 or num < 0
    print("numero fuera de rango ")
    
    
    
