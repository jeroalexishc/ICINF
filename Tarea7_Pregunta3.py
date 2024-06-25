supermercado={}

print("\n--- Fase de Ingreso (o presione Enter para finalizar) ---")
while True:
    nombre=input("ingrese nombre del producto: ")
    if nombre=="":
        break
    cantidad=int(input("ingrese la cantidad de productos: "))
    supermercado[nombre]=cantidad

print("\n--- Fase de produccion --- ")
multiplicador=int(input("ingrese multiplicador de productos: "))

for cantidad in supermercado:
    supermercado[cantidad] *= multiplicador


print("\nInventario Final: ")
for nombre, cantidad in supermercado.items():
    print(nombre + " = " + str(cantidad))

