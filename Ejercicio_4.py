n=int(input("ingrese la cantidad de trabajadores "))

p=0
cantidad_A=0
cantidad_B=0
suma=0

while p < n:
    s=int(input("ingrese el sueldo del trabajador "))
    if s == -1:
        break
    p+=1

    if s >= 900000:
        cantidad_A+=1
        suma+=s
        
    else:
        if s >= 500000 and s <= 900000:
            cantidad_B+=1
            suma+=s

print("La cantidad de trabajadores que cobran mas de $900.000 son: ",cantidad_A)
print("La cantidad de trabajadores que cobran entre $500.000 y $900.000 son: ",cantidad_B)
print("Gasto Empresarial total por personal: ", suma)
