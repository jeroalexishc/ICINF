numeros=[]

for i in range(10):
    valor=int(input("ingrese numero " + str(i+1) + " : "))
    numeros.append(valor)

print("Los numeros en orden inverso son:")
for valor in reversed(numeros):
    print(valor)
